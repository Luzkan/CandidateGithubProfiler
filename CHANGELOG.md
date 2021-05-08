# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2021-05-08

### Added

- New Script: [`scrape.py`](.src/gitprofiler/py_scripts/scrape.py)
  - The script takes on input output file which can be generated via [**Mega Linter**](https://github.com/nvuillam/mega-linter) by redirecting the standard output stream into a text file _(`> output.txt`)_.
  - Script parses the log data and scrapes **duplicates** table informations into `dictionary`:
    ```python
    {
        "language": str,
        "files": int,         # amount of detected files in given language by linter
        "lines": int,         # amount of detected lines in a given language
        "tokens": int,        # amount of detected tokens ("chars") in a given language
        "clones": int,
        "duplicate_lines_num": int,
        "duplicate_lines_percent": float,
        "duplicate_tokens_num": int,
        "duplicate_tokens_percent": float
    },
    ```
  - Script parses the log data and scrapes **summary** table informations into `dictionary`:
    ```python
    {
        "language": str,
        "linter": str,
        "files": int or str,  # amount of detected files in given language by linter
        "fixed": int,         # amount of fixed errors automatically by linter
        "errors": int         # amount of errors that could not be fixed by linter
    },
    ```
  - All available informations are properly parsed and saved as `output.json` file that contains list of the previously mentioned dictionaries.
- New File: [`CHANGELOG.md`](.)
  - This file serves as a diary of the progress of the programming side of this project.

### Changed

- Added new `README.md` entry about the new script file. It contains the informations about the requirements needed in order to run the script as well as the run process itself with the expected output data.

## [0.2.0] - 2021-05-08

## [0.1.0] - 2021-05-08

## [0.0.1] - 2021-05-08

[unreleased]: https://github.com/pwr-pbr21/M1/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/pwr-pbr21/M1/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/pwr-pbr21/M1/compare/v0.1.0...v0.2.0
[0.1.0]: hhttps://github.com/pwr-pbr21/M1/releases/tag/v0.2.0
