# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [[1.0.2]] - 2021-06-20 _(Marcel Jerzyk)_

### Added

- Research Paper _"Evaluating the Potential of a Candidate for a Job Offer Based on his GitHub Profile"_ in `.pdf` format ([here](./ResearchPaper.pdf)).

### Changed

- Updated [`README.md`](./REAMDE.md) with information about the [`ReasearchPaper.pdf`](./ResearchPaper.pdf).

## [[1.0.1]] - 2021-06-20 _(Marcel Jerzyk)_

### Added

- One more idea in the _Further Reasearch_ in [`conclusions.tex`](./paper/sections/conclusions.tex) section.
- Report #2 file ([`report_2_for_group_m2.tex`](.paper/misc/archive/report_2_for_group_m2.tex)) to the [`archive`](.paper/misc/archive) directory.

### Fixed

- Added missing paper images to the repository.

## [[1.0.0]] - 2021-06-20 _(Marcel Jerzyk)_

Final release.

### Added

- Some final formatting to the paper like page breaks where it would make the article look better.
- Added self-defined formatting for code listings so it doesn't look as bad and highlights keywords, comments and strings properly.

### Changed

- Updated `abstract.tex` with _Results_.
- The final amount of sample size used in algorithms was added (`creating_ml_model.tex`).
- Explanation what `R` script do was added to the `data_collection.tex`
- Removed unused reference.

### Removed

- Older versions of sections in the `paper/misc/archive` directory.

## [[0.11.2]] - 2021-06-17 _(Marcel Jerzyk)_

### Changed

- For privacy, removed the github links and usernames from data files.

## [[0.11.1]] - 2021-06-17 _(Marcel Jerzyk)_

### Changed

- Changed names of the files to be less ambiguous.
- Rebase, changelog entries.

### Removed

- Empty `reproduction` directory.
- Token from `repo_data.r`

## [[0.11.0]] - 2021-06-17 _(Jakub Litkowski)_

### Added

- New [`extract_data_from_git.r`](./src/gitprofiler/r_scripts/extract_data_from_git.r) script added.
- New [`cleaned_data_with_ql.csv`](./data/cleaned_data_with_ql.csv)

## [[0.10.1]] - 2021-06-17 _(Marcel Jerzyk)_

### Changed

- Moved `model_script.r` from _`./reproduction`_ into [`./src/gitprofiler/r_scripts/`](./src/gitprofiler/r_scripts/) directory
- Moved & renamed `model_data_no_labels.csv` from `./reproduction` into [`./data/`](./data) directory.
- Rebase, changelog entries and tweak & [`./README.md`](./README.md) update regarding reproduction.

## [[0.10.0]] - 2021-06-17 _(Jakub Szańca)_

### Added

- `model_script.R` for reproduction purposes
- `modelDataNoLabels.csv` for reproduction purposes

## [[0.9.0]] - 2021-06-17 _(Marcel Jerzyk)_

### Added

- [`conclusions.tex`](./paper/sections/conclusions.tex) section written & translated.
- [`discussion.tex`](./paper/sections/discussion.tex) section written & translated.
- [`results.tex`](./paper/sections/discussion.tex) section written & translated.
- _Conclusion_ written in [`abstract.tex`](./paper/sections/discussion.tex) section.

### Changed

- Added `url` formatting in paper.

### Fixed

- Cropped image in _systematic review_ section and adjusted the width.

## [[0.8.1b]] - 2021-06-15 _(Marcel Jerzyk & Jakub Litkowski)_

### Added

- [`README.md`](./README.md) updated with reproduction instruction for groups `M2`, `M3` & `M4`.

## [[0.8.1a]] - 2021-06-13 _(Marcel Jerzyk)_

### Changed

- Added `pandas`, `numpy`, `requests` and `gitpython` as required packages in `requirements.txt`.

## [[0.8.1]] - 2021-06-13 _(Marcel Jerzyk)_

### Added

- In `README.md`: information about the paper directory.

### Changed

- Moved `/literature/` under the `./data` directory.

### Fixed

- Spelling in `CHANGELOG.md`

## [[0.8.0]] - 2021-06-13 _(Marcel Jerzyk)_

### Changes

Further work on the paper:

- Creating _Machine Learning Model_ section created
- First results are available in _Results_ section
- Whole paper was re-checked via grammar checker and adjusted accordingly
- Whole paper got "lifting" via improved formatting
- Sections got labels so they can be cross-referenced for improved "user reading experience"
- Improved language and added contents in Data Processing section
  - Among others, details regarding manual pre-processing of questionnaire.

### Added

- _Data_ section in [**`README.md`**](./README.md)

## [[0.7.2]] - 2021-06-13 _(Marcel Jerzyk)_

### Added

Used literature as `.pdf`s in the [./data/literature/](./data/literature) directory

## [[0.7.1]] - 2021-06-04 _(Marcel Jerzyk)_

### Changed

- Literature Review was retranslated to formal ,,paper'' English.

## [[0.7.0]] - 2021-06-02 _(Marcel Jerzyk)_

### Added

- New script: [`.../merge_jsons.py`](./src/git_profiler/py_scripts/merge_jsons.py) was added to the project.

  - This script takes on input:
    - `str:` **`github_username`**,
  - Output is stored _(by default)_ in:
    - [`.data/scanned_user/`**`<username>`**`.json`](.data/scanned_user/)
  - The purpose of this script is to merge all of the `.json` files that are generated via [`.../scan_repositories.py`](./src/git_profiler/py_scripts/scan_repositories.py) script into one `.json` file that contains merged information from all of them in a 'gather' mode. This means that when in some other file information fetched by given combo of **language-linter** is present, then the results are summed up. This allows for even easier usage of the Mega Linter information via ML model because the processing work is already done.
  - The script also takes care of different `.json`-s as some of them are linter-related but others contain aggregated results.
  - Structure of the file is as follows:

    ```python
    {
      "<lang>": {
        "<linter>": {
          "errors": int,
          "files": int,
          "fixed": int
        },
        "total": {
          "clones": int,
          "duplicate_lines_num": int,
          "duplicate_tokens_num": int,
          "files": int,
          "lines": int,
          "tokens": int
        }
      }
    }
    ```

    - There's special case for `<lang>` which is **`"Total:"`** - it contains all aggregated results.
    - The `"total"` subkey doesn't always have to exist, for examples it does not in `<lang>`: `cspell`, `xml`, `yaml`.

  - Example final output:
    ```json
    {
      "Total:": {
        "total": {
          "clones": 163,
          "duplicate_lines_num": 6061,
          "duplicate_tokens_num": 52202,
          "files": 428,
          "lines": 44590,
          "tokens": 473152
        }
      },
      "java": {
        "checkstyle": {
          "errors": 108,
          "files": 109,
          "fixed": 0
        },
        "total": {
          "clones": 56,
          "duplicate_lines_num": 948,
          "duplicate_tokens_num": 10656,
          "files": 106,
          "lines": 11093,
          "tokens": 106282
        }
      },
      "python": {
        "black": {
          "errors": 59,
          "files": 62,
          "fixed": 0
        },
        "flake8": {
          "errors": 2438,
          "files": 62,
          "fixed": 0
        },
        "isort": {
          "errors": 37,
          "files": 62,
          "fixed": 0
        },
        "pylint": {
          "errors": 2,
          "files": 62,
          "fixed": 0
        },
        "total": {
          "clones": 40,
          "duplicate_lines_num": 798,
          "duplicate_tokens_num": 8403,
          "files": 58,
          "lines": 6111,
          "tokens": 57864
        }
      },
      "spell": {
        "cspell": {
          "errors": 9555,
          "files": 640,
          "fixed": 0
        },
        "misspell": {
          "errors": 18,
          "files": 640,
          "fixed": 0
        }
      }
    }
    ```

- Added `paper` directory.
  - It contains the _LaTeX_ paper which got complete overhaul.
  - Redundant text and formatting was removed.
  - Comments that were pointless were removed and existing comments were standardized
  - Moved sections of paper to separate files.
  - Adjusted heading/title sections.
  - Resolved few errors and warnings.
  - Created directory `/img/` for images.
  - Created `/misc/` folder for all the stuff that is not tightly related to the paper or structure.

### Changed

- Script [`.../scan_repositories.py`](./src/git_profiler/py_scripts/scan_repositories.py) now fetches repositories of given user automatically _(no need to provide separate repositories list in order to fetch them)_
  - New input:
    - `str:` **`github_username`**,

## [[0.6.0]] - 2021-05-25 _(Marcel Jerzyk)_

### Added

- New script: [`.../scan_repositories.py`](./src/git_profiler/py_scripts/scan_repositories.py) was added to the project.
  - This script takes on input:
    - `str:` **`github username`**,
    - `list[str]`: **`github repositories names`**
  - It automates the repositories cloning, Mega Linter linting and Mega Linter Scraper scraping routine. It does exactly as what the intuition might suggest:
    - first starts `git clone` on every single repository name given on input
    - then it uses _MegaLinter_ to parse the repositories contents and generate na output file
    - and at the end - uses the previously made [`.../scraper.py`](./src/git_profiler/py_scripts/scraper.py) to parse the file contents into a machine-readable `.json` format
  - The output results are stored in `/data/repositories/<username>` \_(the directory will be automatically created if it's not present yet)\_
  - The script will also try to clean the repositories directory from directories generated by earlier launches.

## [[0.5.0]] - 2021-05-11 _(Marcel Jerzyk)_

### Added

- New directory: [`./docs`](./docs) containing various files regarding the technical side of the project as well as images used in markdown files.
- LaTeX document changes tracker: [`LANGv1.md`](./docs/LANGv1.md). It has previous versions of sections and subsections:
  - Systematic Review
  - Research Questions
  - Resources to Be Searched
  - Results Selection Process
  - Data Collection
  - Data Pre-processing

### Changed

- Moved directory: [`./img/readme/*`](./img/readme/) inside [`./docs`](./docs) _(now: [`./docs/img/readme/*`])_.

## [[0.4.0]] - 2021-05-11 _(Marcel Jerzyk)_

This changelog entry will be filled in a few days.

### Added

- [`data/cleaned_data.csv`](./data/cleaned_data.csv)
- [`data/questionnaire.csv`](./data/questionnaire.csv)
- [`src/gitprofiler/py_scripts/questionnaire_adjuster.py`](./src/gitprofiler/py_scripts/questionnaire_adjuster.py)

## [[0.3.1]] - 2021-05-08 _(Marcel Jerzyk)_

### Added

- Logged in this file Version History for [`0.3.1`](#0.3.1).
- Logged in this file Version History for [`0.3.0`](#0.2.1).
- Logged in this file Version History for [`0.2.1`](#0.2.1).
- Logged in this file Version History for [`0.2.0`](#0.2.0).
- Logged in this file Version History for [`0.1.0`](#0.1.0).
- Logged in this file Version History for [`0.0.1`](#0.0.1).

### Fixed

- Version Number in [`README.md`](./README.md).

## [[0.3.0]] - 2021-05-08 _(Marcel Jerzyk)_

### Added

- New Script: [`scrape.py`](.src/gitprofiler/py_scripts/scrape.py)
  - The script takes on input output file which can be generated via [**Mega Linter**](https://github.com/nvuillam/mega-linter) by redirecting the standard output stream into a text file _(`> output.txt`)_.
  - Script parses the log data and scrapes **duplicates** table information into `dictionary`:
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
  - Script parses the log data and scrapes **summary** table information into `dictionary`:
    ```python
    {
        "language": str,
        "linter": str,
        "files": int or str,  # amount of detected files in given language by linter
        "fixed": int,         # amount of fixed errors automatically by linter
        "errors": int         # amount of errors that could not be fixed by linter
    },
    ```
  - All available information are properly parsed and saved as `output.json` file that contains list of the previously mentioned dictionaries.
- New File: [`CHANGELOG.md`](.)
  - This file serves as a diary of the progress of the programming side of this project.

### Changed

- Added new [`README.md`](./README.md) entry about the new script file. It contains the information about the requirements needed in order to run the script as well as the run process itself with the expected output data.

## [[0.2.3]] - 2021-05-04 _(Marcel Jerzyk)_

### Added

- **`README.md`**:
  - Tutorial on how to install [**Docker**](https://www.docker.com/) environment.
  - Tutorial on how to run [**Mega Linter**](https://github.com/nvuillam/mega-linter) locally on own repository.

## [[0.2.2]] - 2021-04-26 _(Jakub Litkowski)_

### Fixed

- Fixed: _`value is missing where true / false is required`_
- Fixed: _`arguments suggest a different number of lines: 1, 5, 0`_

## [[0.2.1]] - 2021-04-26 _(Marcel Jerzyk)_

### Added

- **`README.md`**:
  - Added information & created `.gif` files for group **M2** that should work as exhaustive instruction on how to use the [**R Studio**](https://www.rstudio.com/).
    - **Tutorial**: How to generate own GitHub Token.
    - **Instruction**: Installing R Studio.
    - Navigating in R Studio.
  - Added tutorial & created `.gif` files that contain exhaustive information on how to use [**Mega Linter**](https://github.com/nvuillam/mega-linter) through **Github Actions**.
    - Information about the _CI_ file and what contents it should have _(including snippet for easy copy-paste)_.
    - Step by step actions in order to trigger the CI/CD Pipeline in [GitHub.com](https://github.com/) on own repository with **Mega Linter** job.

## [[0.2.0]] - 2021-04-20 _(Jakub Litkowski)_

### Added

- GraphQL Query Created
- Scraped information from Query into variables:

  - Bio:

  ```r
  repositoriesNames <- json$data$repositoryOwner$repositories$edges$node$name
  bio               <- json$data$repositoryOwner$bio
  isHireable        <- json$data$repositoryOwner$isHireable
  emptyRepos        <- json$data$repositoryOwner$repositories$edges$node$isEmpty
  commitMsgE        <- json$data$repositoryOwner$repositories$edges$node$defaultBranchRef$target$history$edges
  ```

  - Commit Messages:

  ```r
  commitMSGList     <- list()
  commitDates       <- list()

  for(d in commitMsgE) {
    for(i in 1:length(d$node$author$user$login)){
      if( d$node$author$user$login[i] == "Luzkan"){
        commitDates <- c(commitDates,d$node$committedDate[i])
      }
    }
  }

  for (p in commitMsgE) {
    for(i in 1:length(p$node$author$user$login)){
      if( p$node$author$user$login[i] == "Luzkan"){
        commitMSGList <- c(commitMSGList,p$node$message[i])
      }
    }
  }
  ```

  - Used Languages:

  ```r
  languages <- json$data$repositoryOwner$repositories$edges$node$languages$edges
  languagesList <- list()

  for (l in languages) {
    print(l)
    languagesList <- c(languagesList, l$node$name )
  }
  ```

- Calculating Time Between Commits:

  ```r
  time_between_commits <- list()

  for(idx in seq_along(commitDates)){
    if (idx+1 > length(commitDates)){
        break
    }
    dateOne<-as.POSIXct(commitDates[[idx]], format = "%Y-%m-%dT%H:%M:%SZ")
    dateTwo<-as.POSIXct(commitDates[[idx+1]], format = "%Y-%m-%dT%H:%M:%SZ")
    time_between_commits[[idx]]<- as.numeric(difftime(dateOne,dateTwo, units="mins"))
  }

  average_time_between_commit <- mean(unlist(time_between_commits))
  ```

## [[0.1.0]] - 2021-03-16 _(Marcel Jerzyk)_

### Added

- Created [**`README.md`**](./README.md) for the project that contains various useful information, requirements and instructions in order ot run the program.
- Created initial file structure.
- **`github_graphql.r`** file:

  - Added imports that are required for GraphQL query creation:

  ```r
  library("ghql")
  library("jsonlite")
  library("dplyr")
  ```

  - GraphQL Connection Object

  ```r
  # GraphQL Connection Object (GitHub)
  connection <- GraphqlClient$new(
    url = "https://api.github.com/graphql",
    headers = list(Authorization = paste0("Bearer ", token))
  )
  ```

  - Informative Example GraphQL Query

  ```r
  new_query$query('mydata', '{
    repositoryOwner(login:"Luzkan") {
        repositories(first: 5, orderBy: {field:PUSHED_AT,direction:DESC}, isFork:false) {
        edges {
            node {
            name
            stargazers {
                totalCount
            }
            }
        }
        }
    }
    }')
  ```

  - Execution, parsing & writing to `.json` output

  ```r
  # Execute Query
  (result <- connection$exec(new_query$queries$mydata))

  # Parse to more human readable form
  jsonlite::fromJSON(result)

  # Writing to file
  write(result, "output.json")
  ```

## [[0.0.1]] - 2021-03-01 _(Lech Madeyski)_

**Project was initialized.**

[todo]: https://github.com/pwr-pbr21/M1/compare/1.0.2...HEAD
[1.0.2]: https://github.com/pwr-pbr21/M1/compare/1.0.1...1.0.2
[1.0.1]: https://github.com/pwr-pbr21/M1/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/pwr-pbr21/M1/compare/0.11.2...1.0.0
[0.11.2]: https://github.com/pwr-pbr21/M1/compare/0.11.1...0.11.2
[0.11.1]: https://github.com/pwr-pbr21/M1/compare/0.11.0...0.11.1
[0.11.0]: https://github.com/pwr-pbr21/M1/compare/0.10.1...0.11.0
[0.10.1]: https://github.com/pwr-pbr21/M1/compare/0.10.0...0.10.1
[0.10.0]: https://github.com/pwr-pbr21/M1/compare/0.9.0...0.10.0
[0.9.0]: https://github.com/pwr-pbr21/M1/compare/0.8.1b...0.9.0
[0.8.1b]: https://github.com/pwr-pbr21/M1/compare/0.8.1a...0.8.1b
[0.8.1a]: https://github.com/pwr-pbr21/M1/compare/0.8.1...0.8.1a
[0.8.1]: https://github.com/pwr-pbr21/M1/compare/0.8.0...0.8.1
[0.8.0]: https://github.com/pwr-pbr21/M1/compare/0.7.2...0.8.0
[0.7.2]: https://github.com/pwr-pbr21/M1/compare/0.7.1...0.7.2
[0.7.1]: https://github.com/pwr-pbr21/M1/compare/0.7.0...0.7.1
[0.7.0]: https://github.com/pwr-pbr21/M1/compare/0.6.0...0.7.0
[0.6.0]: https://github.com/pwr-pbr21/M1/compare/0.5.0...0.6.0
[0.5.0]: https://github.com/pwr-pbr21/M1/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/pwr-pbr21/M1/compare/0.3.1...0.4.0
[0.3.1]: https://github.com/pwr-pbr21/M1/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/pwr-pbr21/M1/compare/0.2.3...0.3.0
[0.2.3]: https://github.com/pwr-pbr21/M1/compare/0.2.2...0.2.3
[0.2.2]: https://github.com/pwr-pbr21/M1/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/pwr-pbr21/M1/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/pwr-pbr21/M1/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/pwr-pbr21/M1/compare/0.0.1...0.1.0
[0.0.1]: https://github.com/pwr-pbr21/M1/releases/tag/0.0.1
