# M1-2022-git

## Introduction
Welcome to this exercise about git bissect and pull requests.
This repository is made of 3 branches :
 * main
 * dev
 * decimal-binary-converter

A binary/decimal two-way converter has been implemented in this repository. It is still in a development stage, in its feature branch.

## Getting started
You should be working from **your own repository** that is a fork of M1-2022-git.
In order to run this project, you will have to follow these steps.
1. Clone this project
2. move into the project folder
``` shell
cd M1-2022-git
```
3. Set up a virtual environment
 * Create the virtual environment
 ```shell
 python -m venv myvenv
 ```
 * Activate venv
 ```shell
 . venv/bin/activate
 ```
4. Install pytest
```shell
pip install -U pytest
```
5. Execute main script
```shell
python main.py
```

## Instructions
### Report issues
Now, you'll have to experiment with the repo.

1. Inspect the different branches and find where the code of the converter is
2. Run the converter code
3. You may notice that the code contains some bugs. The code lacks some unit tests to expose such bugs. We will create some :
 * Create a file whose name starts with *test_*
 * Inside that file, create a class. The class name must have the prefix *Test* and the class must inherit unittest.TestCase (do not forget to import unittest package)
  * Inside that class, Define test methods for each function of the converter. Each test method must have a name starting with test_ (again).
4. Inside your terminal (you should be in your project directory), run :
```shell
pytest
```
This will execute the tests you have written and show you a test report.

5. On Github, on the original repository, open an issue about the bugs you found. Remember to be specific about the problem. You should also include code to reproduce the issue

### Find bugs
6. Using *git bisect*, find which commit is faulty, introducing those bugs. Reminder : to use *git bisect*, ensure that the bug is present at the commit you're at. If so, type 
```shell
git bisect bad
```
Then, find an old commit where the code had no bug (use *git checkout* to navigate from one commit to another. Do not hesitate to go far in the past : the interest of git bisect is that you won't have to test one commit after another, so take an old commit (maybe when the feature was introduced) and let git do the magic. When you've found a commit where the bugs are not present, you can execute 
```shell
git bisect good
```
Now, git knows where to start (it has a buggy commit and a clean commit). So, you can execute :
```shell
git bisect start
```
Git will navigate through commits using Binary Search. For each step, run the tests. If the tests are KO, type *git bisect bad* else *git bisect good*. After a few steps, git will tell you what commit is faulty.

7. Once you've found the faulty commit, find what lines are responsible of the bugs and fix them. If you've fixed all the bugs, all Unit Tests should return OK when pytest is run

### Pull request
8. Once the code is fixed, you can commit your work and open a Pull Request on GitHub so that the maintainer of the original repository can review your code and eventually merge it into its repo.
9. Congratulations, you've contributed to your first Open Sources project
