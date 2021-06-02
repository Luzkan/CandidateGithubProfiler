from typing import List
from subprocess import Popen
import argparse
import logging as log
import asyncio
from pathlib import Path
from scraper import MegaLinterScraper
from github import Github
import shutil


NODEJS_PATH = r'C:\Program Files\nodejs\npx.cmd'
REPOSITORIES_DIR = "./data/repositories"
DELAY = 3


def subprocess_run(args_list: list[str], username: str, cwd_path: Path = None, stdout_path: Path = None) -> None:
    """ Executes commands in given ./data/repostiries/{username}

    Args:
        args_list (list): List of Shell arguments which shall be executed
        username (str):   GitHub username of versionised user
        cwd_path (Path, default: None):
        stdout_path (Path, default: None):
    """
    if not cwd_path:
        cwd_path = Path(f"{REPOSITORIES_DIR}/{username}")
        cwd_path.mkdir(parents=True, exist_ok=True)

    try:
        if stdout_path:
            with open(stdout_path, "w") as output_file:
                Popen(args=args_list, cwd=cwd_path, stdout=output_file)
        Popen(args=args_list, cwd=cwd_path)
    except NotADirectoryError:
        log.error("Error: Wrong directory path.")


async def fetch_repositories(username: str) -> None:
    """ Fetches given GitHub user repositories into ./data/repositories/<username> directory.

    Args:
        username (str): GitHub username
        repositories (list[str]): List of repositories names
    """
    g = Github()

    for repository in g.get_user(username).get_repos():
        repo = g.get_repo(f"{username}/{repository.name}")

        log.info(f"Cloning {repository}.")
        subprocess_run(["git", "clone", repo.clone_url], username)


def get_repositories_directory_size() -> int:
    """ Returns integer which is current filesize of Repositories directory """
    return sum(f.stat().st_size for f in Path(REPOSITORIES_DIR).glob('**/*') if f.is_file())


async def wait_for_repos(task: asyncio.Task, msg: str):
    """ Waits until other threads are done with fetching/generating things in the
    ./data/repositories/* directory. It is done by checking the current filesize of
    the catalogue and comparing if filesize has changed after DELAY/2 seconds.

    Args:
        task (asyncio.Task): Task which is awaited.
        msg (str): Message indicating what we wait for (for logging purposes).
    """
    last_dir_size = get_repositories_directory_size()
    await task
    await asyncio.sleep(DELAY/2)
    curr_dir_size = get_repositories_directory_size()

    while last_dir_size != curr_dir_size:
        await asyncio.sleep(DELAY)
        log.info(f"Repositories are still being {msg}... ({last_dir_size} -> {curr_dir_size})")
        last_dir_size = curr_dir_size
        curr_dir_size = get_repositories_directory_size()
    log.info(f"All Repositories {msg} {last_dir_size} / {curr_dir_size}")


async def lint_repositories(username: str) -> List[Path]:
    user_repositories_path = Path(f'{REPOSITORIES_DIR}/{username}')
    local_repo_paths = [repo for repo in user_repositories_path.iterdir() if repo.is_dir()]
    output_files = []

    for local_repo_path in local_repo_paths:
        log.info(f"Running linter in: {local_repo_path.name} ({local_repo_path})")
        node_exe_path = Path(NODEJS_PATH)
        cmd_lint = f"{node_exe_path} mega-linter-runner"
        cmd_flavour = "--flavor all"
        cmd_e = "-e 'SHOW_ELAPSED_TIME=true'"
        output_file = Path(f'{local_repo_path}/{username}-{local_repo_path.name}.txt')
        cmd = f"{cmd_lint} {cmd_flavour} {cmd_e}".split(" ")
        log.info(f"Command: {cmd}")
        subprocess_run(cmd, username, local_repo_path, output_file)
        output_files.append(output_file)

    return output_files


async def parse_linted_output_tables(linter_output_filepaths: List[Path]) -> List[Path]:
    """ Uses MegaLinterScraper to parse generated linter output text files.

    Args:
        linter_output_filepaths (List[Path]): List of filepaths to MegaLinter output text files.

    Returns:
        List[Path]: List of filepaths to .jsons parsed by MegaLinterSraper.
    """
    mls = MegaLinterScraper()
    linted_filepaths = []
    for output_file in linter_output_filepaths:
        log.info(f"Parsing linter log for repository {output_file.name}.")
        linted_filepath = f"{output_file.parents[0]}/{output_file.stem}.json"
        mls.run(output_file.name, output_file.parents[0], linted_filepath)
        linted_filepaths.append(Path(linted_filepath))
        log.info(f"Parsed linted file: {output_file.name}.")
    return linted_filepaths


async def clean_data_directory(parsed_filepaths: List[Path]) -> None:
    """ Moves parsed .json files outside the repository directory one
    directory above (into: ./data/repositories/<username>).
    Then attemps to remove the cloned repositories from disk leaving
    only the parsed .json files.

    Args:
        parsed_filepaths (List[Path]): List of filepaths to parsed .json's
    """
    for filepath in parsed_filepaths:
        shutil.move(filepath, f"{filepath.parents[1]}/{filepath.name}")

    if parsed_filepaths:
        p = Path(parsed_filepaths[0].parents[1]).glob('*/')
        directories = [x for x in p if x.is_dir()]

        for file in directories:
            try:
                shutil.rmtree(file)
            except OSError:
                log.warning(f"Couldn't remove: {file}")


async def main(username: str) -> None:
    task_fetch = asyncio.create_task(fetch_repositories(username))
    await wait_for_repos(task_fetch, "fetched")
    linter_output_filepaths = asyncio.create_task(lint_repositories(username))
    await wait_for_repos(linter_output_filepaths, "linted")
    parsed_output_filepaths = asyncio.create_task(parse_linted_output_tables(linter_output_filepaths.result()))
    await parsed_output_filepaths
    await asyncio.create_task(clean_data_directory(parsed_output_filepaths.result()))
    log.info("Success.")


def arguments_parser() -> argparse.Namespace:
    """ Parses arguments. """
    parser = argparse.ArgumentParser(description="Input File containing list of repositories url's")
    parser.add_argument("-u", "--username", default='Luzkan',
                        help="GitHub Username. \
                        (default: %(default)s)")
    parser.add_argument("-r", "--repositories", default=['DeveloperEnvironment', 'PythonCourse'], nargs='*',
                        help="List of repository names that should be linted. \
                        (default: %(default)s)")
    return parser.parse_args()


def init():
    # Logger
    log.root.setLevel(log.INFO)
    handler = log.StreamHandler()
    handler.setFormatter(log.Formatter(fmt='[%(asctime)-15s] %(levelname)-8s|  %(message)s'))
    log.root.addHandler(handler)

    # Args
    arguments = arguments_parser()

    # Run
    asyncio.run(main(arguments.username))


if __name__ == "__main__":
    init()
