# Advent of Code 2017

Contains my personal solutions to Advent of code problems.

Advent of code is hosted on http://adventofcode.com

## Usage

This projects assumes having inputs named ```input/dayXY``` at the root, where ```X``` is the number of the day and ```Y``` is the letter of the problem for the day.
Example : ```input/day03b```

To run the app, you need to have Python 3 installed
Simply run ```python main.py```, then input the desired problem number when asked

Example :
```
10:47 - grasseh:~/adventofcode-2017 (master) - python3 main.py
Welcome to Grasseh's 2017 Advent of Code
Enter your problem number
>00a
The solution to problem 00a is : 21
Execution complete in     0.0186 ms
```

## Units tests

Tests are written in the solver files. They can be run using

```
python3 -m unittest discover -s solvers -p '*.py'
```

or
```
bash tests
```

## Performance

Each problem has been ran 1000 times. The average can be found in this [file](/performance.md)
