# Python Samples

##### Requirements
- python 3.x
- pip3
- pipenv

##### Optional
- virtualenv

Process for `python3.x`
```
> python3 --version

If not installed

LINUX:
> sudo apt-get install python3

MACOS
> brew install python3
```

Process for `pip3`
```
> pip3 --version

If not installed
> sudo apt-get install python3-pip

OR

> curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
> python3 get-pip.py --user
```

Process for `pipenv`
```
> pipenv --version

If not installed
> pip3 install pipenv
```

Installation
> pipenv install -d

Run
```
via pipenv
> pipenv run python3 samples/<file>.py

OR

If virtualenv is activated
> python3 samples/<file>.py
```

Activate virtualenv
```
> source `pipenv --venv`/bin/activate
```
