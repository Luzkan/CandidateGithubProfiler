from __future__ import annotations
import json
import os
import argparse


class JSONSMerger():
    def __init__(self, username: str, directory: str = './data/repositories/'):
        self.directory = f"{directory}/{username}"
        self.username = username
        self.json = {}

    def merge_all(self):
        for file_path in os.listdir(self.directory):
            if file_path.endswith(".json") and file_path.startswith(self.username):
                self.merge(file_path)

    def merge(self, json_path: str):
        merging_json = self.open_json(json_path)
        for info in merging_json:
            if "linter" in info:
                self.merge_linter(info)
            else:
                self.merge_total(info)

    # * -=-=-=-=-=-=-=-=-=-=-=-
    # Merging related to linter parsed results

    def merge_linter(self, info: dict):
        if info["language"] in self.json and info["linter"] in self.json[info["language"]]:
            self.linter_blend(info)
            return

        self.linter_adjoin(info)

    def linter_adjoin(self, info: dict):
        if not info["language"] in self.json:
            self.json[info["language"]] = {}

        self.json[info["language"]][info["linter"]] = {}
        new_entry = self.json[info["language"]][info["linter"]]
        new_entry["files"] = info["files"]
        new_entry["fixed"] = info["fixed"] if info["fixed"] else 0
        new_entry["errors"] = info["errors"]

    def linter_blend(self, info: dict):
        new_entry = self.json[info["language"]][info["linter"]]
        new_entry["files"] += info["files"]
        new_entry["fixed"] += info["fixed"] if info["fixed"] else 0
        new_entry["errors"] += info["errors"]

    # * -=-=-=-=-=-=-=-=-=-=-=-
    # Merging related to total parsed results

    def merge_total(self, info: dict):
        if info["language"] in self.json and "total" in self.json[info["language"]]:
            self.total_blend(info)
            return

        self.total_adjoin(info)

    def total_adjoin(self, info: dict):
        if not info["language"] in self.json:
            self.json[info["language"]] = {}

        self.json[info["language"]]["total"] = {}
        new_entry = self.json[info["language"]]["total"]
        new_entry["files"] = info["files"]
        new_entry["lines"] = info["lines"]
        new_entry["tokens"] = info["tokens"]
        new_entry["clones"] = info["clones"]
        new_entry["duplicate_lines_num"] = info["duplicate_lines_num"]
        new_entry["duplicate_tokens_num"] = info["duplicate_tokens_num"]
        # Obviously stacking duplicate percentages doesn't make any sense.
        # new_entry["duplicate_lines_percent"] = info["duplicate_lines_percent"]
        # new_entry["duplicate_tokens_percent"] = info["duplicate_tokens_percent"]

    def total_blend(self, info: dict):
        new_entry = self.json[info["language"]]["total"]
        new_entry["files"] += info["files"]
        new_entry["lines"] += info["lines"]
        new_entry["tokens"] += info["tokens"]
        new_entry["clones"] += info["clones"]
        new_entry["duplicate_lines_num"] += info["duplicate_lines_num"]
        new_entry["duplicate_tokens_num"] += info["duplicate_tokens_num"]
        # Obviously stacking duplicate percentages doesn't make any sense.
        # new_entry["duplicate_lines_percent"] += info["duplicate_lines_percent"]
        # new_entry["duplicate_tokens_percent"] += info["duplicate_tokens_percent"]

    # * -=-=-=-=-=-=-=-=-=-=-=-
    # Utility Functions

    def open_json(self, filename: str) -> dict | None:
        """Opens up JSON file in the same directory.

        Args:
            file_path (str): json file name

        Returns:
            dict: loaded json as dictionary
        """
        json_path = os.path.join(self.directory, filename)
        try:
            with open(json_path, "r") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"Couldn't find {filename}. (path: {json_path}) file.")
        return None

    def save_json(self, output_filename: str, indent: int = 4):
        """ Saves currently stored json in the class to file

        Args:
            output_filename (str): the name of output json file
        """
        with open(f'{self.directory}/{output_filename}.json', 'w') as json_file:
            json.dump(self.json, json_file, indent=indent, sort_keys=True)
        print(f"Succesfully parsed and saved as {json_file.name}.")

    def print(self, indent: int = 2):
        """ Printsout currently stored json in the class. """
        print(json.dumps(self.json, indent=indent, sort_keys=True))


def arguments_parser():
    parser = argparse.ArgumentParser(description="Mega Linter Data Scraper")
    parser.add_argument("-u", "--username", default="Luzkan",
                        help="Username (which is name of the directory containing parsed linter .json's). \
                        (default: %(default)s)")
    return parser.parse_args()


def main():
    args = arguments_parser()
    jm = JSONSMerger(args.username)
    jm.merge_all()
    jm.print()
    jm.save_json(f'{args.username}')


if __name__ == "__main__":
    main()
