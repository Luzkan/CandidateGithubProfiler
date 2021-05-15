# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

---

## [[0.5.0]] - 2021-05-11 _(Marcel Jerzyk)_

### Added

- New directory: [`./docs`](./docs) containing various files regarding the technical side of the project as well as images used in markdown files.
- LaTeX document changes tracker: [`LANGv1.md`](./docs/LANGv1.md). It has previous versions of sections and subsections:
  - Systematic Review
  - Research Questions
  - Resources to Be Searched
  - Results Selection Process
  - Literature Review
  - Methodology
  - Data Collection
  - Data Preprocessing

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

- Added new [`README.md`](./README.md) entry about the new script file. It contains the informations about the requirements needed in order to run the script as well as the run process itself with the expected output data.

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
  - Added informations & created `.gif` files for group **M2** that should work as exhaustive instruction on how to use the [**R Studio**](https://www.rstudio.com/).
    - **Tutorial**: How to generate own GitHub Token.
    - **Instruction**: Installing R Studio.
    - Navigating in R Studio.
  - Added tutorial & created `.gif` files that contain exhaustive information on how to use [**Mega Linter**](https://github.com/nvuillam/mega-linter) through **Github Actions**.
    - Informations about the _CI_ file and what contents it should have _(including snippet for easy copy-paste)_.
    - Step by step actions in order to trigger the CI/CD Pipeline in [GitHub.com](https://github.com/) on own repository with **Mega Linter** job.

## [[0.2.0]] - 2021-04-20 _(Jakub Litkowski)_

### Added

- GraphQL Query Created
- Scraped informations from Query into variables:

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

- Created [**`README.md`**](./README.md) for the project that contains various useful informations, requirements and instructions in order ot run the program.
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

[unreleased]: https://github.com/pwr-pbr21/M1/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/pwr-pbr21/M1/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/pwr-pbr21/M1/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/pwr-pbr21/M1/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/pwr-pbr21/M1/compare/v0.2.3...v0.3.0
[0.2.3]: https://github.com/pwr-pbr21/M1/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/pwr-pbr21/M1/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/pwr-pbr21/M1/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/pwr-pbr21/M1/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/pwr-pbr21/M1/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/pwr-pbr21/M1/releases/tag/v0.0.1
