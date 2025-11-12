# Continuous Integration with [unittest](https://docs.python.org/3/library/unittest.html) Starter

## For the Intensive Foundation to Computer Science and Programming course at [Northeastern University London](https://www.nulondon.ac.uk/)

This repository is a resource for learners beginning with continuous integration. It demonstrates how to use [GitHub Actions](https://docs.github.com/en/actions) to automatically run unit tests each time code is pushed to GitHub.

A YAML Action is a configuration file that tells GitHub what to do automatically when certain events occur. Written in YAML, it defines a workflow made of jobs and steps. In this project, the workflow checks out the code, sets up Python, installs any dependencies, and runs all unit tests using Python’s built-in unittest framework.

The repository includes a `.github/workflows/test.yml` file that provides a boilerplate setup for running unit tests in any Python project. You can copy this file into your own repository to enable automated testing without extra setup.

## User Documentation

This repository is not meant for a “classic end-user” audience. Instead, it is a resource for developers—specifically those in the Intensive Foundation to Computer Science and Programming course who want to get started quickly with continuous integration using [unittest](https://docs.python.org/3/library/unittest.html) framework.

Inside you’ll find simple unit tests that exercise various assertions (using Python’s built-in [unittest](https://docs.python.org/3/library/unittest.html)), and a boilerplate [YAML](https://yaml.org/spec/1.2.2/) workflow file (for GitHub Actions) that sets automatic testing in motion on every push to the remote repo.

Think of it like a developer-friendly launch pad: clone or fork the repo, adapt the tests or workflow for your own code, and you’re set up with CI in minutes rather than hours.


