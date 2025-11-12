# Continuous Integration with [unittest](https://docs.python.org/3/library/unittest.html) Starter

## For the Intensive Foundation to Computer Science and Programming course at [Northeastern University London](https://www.nulondon.ac.uk/)

This repository is a resource for learners beginning with continuous integration. It demonstrates how to use [GitHub Actions](https://docs.github.com/en/actions) to automatically run unit tests each time code is pushed to GitHub.

A YAML Action is a configuration file that tells GitHub what to do automatically when certain events occur. Written in YAML, it defines a workflow made of jobs and steps. In this project, the workflow checks out the code, sets up Python, installs any dependencies, and runs all unit tests using Python’s built-in unittest framework.

The repository includes a `.github/workflows/test.yml` file that provides a boilerplate setup for running unit tests in any Python project. You can copy this file into your own repository to enable automated testing without extra setup.

## User Documentation

This repository is not meant for a “classic end-user” audience. Instead, it is a resource for developers—specifically those in the Intensive Foundation to Computer Science and Programming course who want to get started quickly with continuous integration using [unittest](https://docs.python.org/3/library/unittest.html) framework.

Inside you’ll find simple unit tests that exercise various assertions (using Python’s built-in [unittest](https://docs.python.org/3/library/unittest.html)), and a boilerplate [YAML](https://yaml.org/spec/1.2.2/) workflow file (for GitHub Actions) that sets automatic testing in motion on every push to the remote repo.

Think of it like a developer-friendly launch pad: clone or fork the repo, adapt the tests or workflow for your own code, and you’re set up with CI in minutes rather than hours.

### Technical Documentation

#### Repository overview

The repository contains the following key components:

- A folder [tests/](https://github.com/EDGENortheastern/if-combined-unittest-resources/tree/main/tests) containing sample unit tests written with Python’s unittest framework.

- A workflow definition in [.github/workflows/test.yml](https://github.com/EDGENortheastern/if-combined-unittest-resources/blob/main/.github/workflows/test.yml) which instructs GitHub Actions to run these tests on every push or pull request.

- A README and license file to document usage and legal terms.

#### YAML workflow file

The file `test.yml` is a YAML (YAML Ain’t Markup Language) configuration file used by GitHub Actions. It defines a workflow, which is triggered by one or more events (such as code being pushed or a pull request being opened). Within the workflow you specify one or more jobs, each of which runs on a specified runner environment (for example, `ubuntu-latest`). Inside each **job**, you list steps, which can include checking out the code, installing dependencies, setting up a runtime (here, Python), and executing commands (here, unit tests).

In this repository’s workflow:

- The workflow triggers on push and pull_request events.

- A job named test runs on the ubuntu-latest runner.

- The steps are: check out the code via `actions/checkout`; set up Python via `actions/setup-python`; optionally install dependencies (via `pip install -r requirements.txt`); then run the tests with `python -m unittest discover -s tests`.

If the tests pass, the job succeeds; if any test fails, the workflow marks failure.


