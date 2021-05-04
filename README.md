<h1 align="center">
  <br>
  Git Profiler <b>v0.1.0</b> <i>(PBR21M1)</i>
  <br>
</h1>

<h4 align="center">Automatic profiler based on GitHub Profile</h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#usage">Usage</a> •
  <a href="#planned">Planned</a> •
  <a href="#planned">Paper</a>
</p>


## __Features__

- GitHub Graph QL Query which gives on output all the data that could be useful in this research.


## __Usage__

### Requirements:

- [R Studio](https://www.rstudio.com/) - Data Science tool with integrated development environment for R language.
- [R Language](https://www.r-project.org/) - programming language and free software environment for statistical computing and graphics
- [GHQL](https://github.com/ropensci/ghql) - a GraphQL client for R
- [MegaLinter](https://github.com/nvuillam/mega-linter) - all-in-one linter solution

<details>
  <summary>Running the R Scripts.</summary>

---

### Running:

Launching New Project.

<img src="./img/readme/loading_project.png" alt="Launching New Project in R Studio" width="850"/>

Navigating to directory containing scripts (`./src/gitprofiler/r_scripts/`).

<img src="./img/readme/scripts_source_dir.gif" alt="Navigating to R Scripts directory" width="850"/>

Open one of the scripts. You have to modify line `10`, which holds the __GitHub Token__ value. You can generate one via [Personal Access Token Page](https://github.com/settings/tokens/new).

<img src="./img/readme/generating_github_token.gif" alt="Generating new Personal GitHub Access Token" width="850"/>

After generating one, replace the string `token <- "`__`<token>`__`"` in order to be able to access GitHub Graph QL.

<img src="./img/readme/inserting_private_token.png" alt="Inserting Private Token" width="850"/>

Console Window when running the Query (`v0.1.0`).

<img src="./img/readme/running_query_v0_1_0.gif" alt="Running Query v0.1.0" width="850"/>

__Results__ can be found in the _Environment_ tab on the right pane.

<img src="./img/readme/query_results_v0_1_0.png" alt="Query Results v0.1.0" width="850"/>

</details>


<details>
  <summary>Running the Mega Linter.</summary>

---

### Current State

At this moment we are investigating incorporating __docker__ into the project so we could make use of the __Mega Linter__ locally. As of `v0.1.0` we tested it through [GitHub CI](https://docs.github.com/en/actions/guides/about-continuous-integration).

### Setup & Run

Choose any repository of yours and clone it to your machine using [`git clone`](https://git-scm.com/docs/git-clone) command. Then proceed:

```cmd
cd <your_project_name>
mkdir .github && cd .github
mkdir workflows && cd workflows
notepad mega-linter.yml
```

Then paste this code snippet below and save the file.

```yaml
name: Mega-Linter

on:
  push:
  pull_request:
    branches: [master, main]

jobs:
  cancel_duplicates:
    name: Cancel duplicate jobs
    runs-on: ubuntu-latest
    steps:
      - uses: fkirc/skip-duplicate-actions@master
        with:
          github_token: ${{ secrets.PAT || secrets.GITHUB_TOKEN }}

  build:
    name: Mega-Linter
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
        with:
          token: ${{ secrets.PAT || secrets.GITHUB_TOKEN }}
          fetch-depth: 0
      - name: Mega-Linter
        id: ml
        uses: nvuillam/mega-linter@v4
        env:
          VALIDATE_ALL_CODEBASE: ${{ github.event_name == 'push' && github.ref == 'refs/heads/master' }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Archive production artifacts
        if: ${{ success() }} || ${{ failure() }}
        uses: actions/upload-artifact@v2
        with:
          name: Mega-Linter reports
          path: |
            report
            mega-linter.log
```

Lastly, push the new workflow into your Remote GitHub Repository with

```bash
git add .
git commit -m "MegaLinter"
git push -f
```

Now, you can open your project through a web browser and navigate to _"Actions"_ tab. You should see the Mega Linter job.

<img src="./img/readme/mega_linter_job.png" alt="Mega Linter Job visible through GitHub CI" width="850"/>

Here's an example result from Mega Linter.

<img src="./img/readme/mega_linter_results.png" alt="Mega Linter Results Table" width="850"/>

</details>

<details>
  <summary><b>Running the Mega Linter locally.</b></summary>

---

## Requirements

__Important Notice:__ Mega Linter is super-heavy in terms of required storage (__`40GB+`__).

As a prerequisite - you have to have [Docker](https://www.docker.com/products/docker-desktop) installed on your computer.

> Windows

First, download the [Linux Kernel Update Package](https://docs.microsoft.com/pl-pl/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package). It is necessary for Docker to work on your machine. Then, download the Docker [executable installer](https://www.docker.com/products/docker-desktop) and install it just like any other application. Restart is mandatory after the installation.

> Unix

Depending on the version of your distro, something analogous to this command should do the job:

```sh
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Running

If you have Docker already installed:

 - clone fresh copy of desired repository which you would like to examine using [`git clone`](https://git-scm.com/docs/git-clone) command.
 - navigate to the repository
 - run this command: `npx mega-linter-runner --flavor all -e 'ENABLE=,DOCKERFILE,MARKDOWN,YAML' -e 'SHOW_ELAPSED_TIME=true'`
 
New directory should be created in the repository called `reports`.

</details>


## __Planned__

TBD.

## __Paper__

TBD.
