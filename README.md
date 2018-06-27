# SamplePytestProject


## Install Python

Download and install python from [Python.org](https://www.python.org/). Version 2 or 3 will work.

## Create Virtual Environment

Run the following commands from the root folder of the forked project. 

```
pip install virtualenv
virtualenv SamplePytestProject
```

Once that completes, also run this command from the same folder.

```
source SamplePytestProject/bin/activate
pip install pytest pytest-runner
python setup.py develop
```

## Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you the failing tests. This is good! We'll be fixing this test once we jump into the build step.

```
python setup.py test
```

Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

# Solution

[sample/app.py](https://github.com/pluralsight-projects/SamplePytestProject/blob/solution/sample/app.py)