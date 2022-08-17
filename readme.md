# Python Coding Assignment

 

## Usage

 

This projects supports four user interaction interfaces

- ### ```main.py``` runs on command prompt,

1. will prompt user to enter choice, enter number from available options

2. will prompt user to enter arguments, enter arguments for the function


 

## Run Tests

Pytest is used for testing class methods, to run Pytest, please keep the code files mimicking the directory structure

mentioned below

```

# run following command in project directory

python -m pytest

```

 

## Directory Structure

```

RaboCodingAssignment

├── src  # python package

│   ├── utils # python package to contain utility modules

│   │   ├── __init__.py   # to make directory into package

│   │   └── utils.py # contains utility functions to process text

│   │
│   ├── WordFrequencyAnalyser# 

│   │  ├── __init__.py   # to make directory into package

│   │  └── WordFrequencyAnalyser.py# contains Executor class to execute

│                                   #WordFrequencyAnalyzer functions

│   

├── tests # test directory

│   │   ├── __init__.py  # to make directory into package

│   │   └── test_WordFrequencyAnalyzer.py    # contains test_inputs

│   │   ├── conftest.py  # contains text fixtures  


├── main.py # command prompt interface for user

└── README.md

```


### Use of 3rd Party Python Libraries

- Flask 1.1.2

- pytest 6.2.3

