from typing import List
from subprocess import Popen
import argparse
import logging as log
import asyncio
from pathlib import Path
from scraper import MegaLinterScraper
from github import Github

REPOSITORIES_DIR = "./data/repositories"
DELAY = 3


def arguments_parser():
    parser = argparse.ArgumentParser(description="Input File containing list of repositories url's")
    parser.add_argument("-u", "--username", default='Luzkan',
                        help="GitHub Username. \
                        (default: %(default)s)")
    parser.add_argument("-r", "--repositories", default=['DeveloperEnvironment', 'PythonCourse'], nargs='*',
                        help="List of repository names that should be linted. \
                        (default: %(default)s)")
    return parser.parse_args()


def subprocess_run(args_list: list, username: str, cwd_path: Path = None, stdout_path: Path = None) -> None:
    """ Executes commands in given ./data/repostiries/{username} """
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


def clone_repository(url: str, username: str) -> None:
    subprocess_run(["git", "clone", url], username)


async def fetch_repositories(username: str, repositories: list) -> None:
    g = Github()

    for repository in repositories:
        repo = g.get_repo(f"{username}/{repository}")

        log.info(f"Cloning {repository}.")
        clone_repository(repo.clone_url, username)


def get_repositories_directory_size() -> int:
    return sum(f.stat().st_size for f in Path(REPOSITORIES_DIR).glob('**/*') if f.is_file())


async def wait_for_repos(task: asyncio.Task, msg: str):
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
        node_exe_path = Path(r'C:\Program Files\nodejs\npx.cmd')
        cmd_lint = f"{node_exe_path} mega-linter-runner"
        cmd_flavour = "--flavor all -e 'ENABLE=,DOCKERFILE,MARKDOWN,YAML'"
        cmd_e = "-e 'SHOW_ELAPSED_TIME=true'"
        output_file = Path(f'{local_repo_path}/{username}-{local_repo_path.name}.txt')
        cmd = f"{cmd_lint} {cmd_flavour} {cmd_e}".split(" ")
        log.info(f"Command: {cmd}")
        subprocess_run(cmd, username, local_repo_path, output_file)
        output_files.append(output_file)

    return output_files


async def parse_linted_output_tables(linter_output_filepaths: List[Path]) -> None:
    mls = MegaLinterScraper()
    print(f"Halo {linter_output_filepaths}")
    for output_file in linter_output_filepaths:
        print(f"Halo: {output_file}")
        log.info(f"Parsing linter log for repository {output_file.name}.")
        mls.run(output_file.name, output_file.parents[0], f"{output_file.parents[0]}/{output_file.stem}.json")
        log.info(f"Parsed lint of {output_file.name} saved in: {output_file.parents[0]}/{output_file.stem}.json")


async def main(username: str, repositories: list) -> None:
    task_fetch = asyncio.create_task(fetch_repositories(username, repositories))
    await wait_for_repos(task_fetch, "fetched")
    linter_output_filepaths = asyncio.create_task(lint_repositories(username))
    await wait_for_repos(linter_output_filepaths, "linted")
    await asyncio.create_task(parse_linted_output_tables(linter_output_filepaths.result()))
    log.info("Success.")


def init():
    # Logger
    log.root.setLevel(log.INFO)
    handler = log.StreamHandler()
    handler.setFormatter(log.Formatter(fmt='[%(asctime)-15s] %(levelname)-6s|  %(message)s'))
    log.root.addHandler(handler)

    # Args
    arguments = arguments_parser()

    # Run
    asyncio.run(main(arguments.username, arguments.repositories))


if __name__ == "__main__":
    init()
