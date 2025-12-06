# Testing Pre-commit YAML
Testing Pre-commmit YAML is a python project aimed at learning the CI/CD flow of linting in projects.

## Getting Started
Ensure you have [python](https://www.python.org/downloads/) and [git](https://git-scm.com/install/) installed on your device before running the below commands.

Once the above tools have been installed, you will use python library manager [pip](https://pip.pypa.io/en/stable/) to install the required dependecies to run the project.

## Dependency Installation

Run the below command to install python dependencies
```bash
pip install -r requirements.txt
```

Run the below command to install pre-commit to the .git/hooks
```bash
pre-commit install
```
## How it Works

Testing Pre Commit will prevent any python code that does not follow the python linting standards from being committed to the remote repository. In most cases where applicable and possible it will refractor the python code to fit the set standard or will direct a user to the script and line where code changes **DO NOT** meet set standards.

_For Example_:
```python
def hello():
    name = input("Enter user name: ")



        print(f"Welcome to Test Pre Commit {name}")
```

Once ran through pre-commit with:
```bash
pre-commit run --all-files
```

the script will be changed to:
```python
def hello():
    name = input("Enter user name: ")

    print(f"Welcome to Test Pre Commit {name}")
```
since this is the standard set format of a python file

