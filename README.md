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

Each problem has been ran 5 times and averaged

| Day | Problem a (ms) | Problem b (ms) |
|-----|---------------:|---------------:|
|1    |0.7355          |0.9158          |
|2    |0.3348          |0.6555          |
|3    |0.0496          |0.3985          |
|4    |1.0981          |4.8254          |
|5    |x.xxxx          |x.xxxx          |
|6    |x.xxxx          |x.xxxx          |
|7    |x.xxxx          |x.xxxx          |
|8    |x.xxxx          |x.xxxx          |
|9    |x.xxxx          |x.xxxx          |
|10   |x.xxxx          |x.xxxx          |
|11   |x.xxxx          |x.xxxx          |
|12   |x.xxxx          |x.xxxx          |
|13   |x.xxxx          |x.xxxx          |
|14   |x.xxxx          |x.xxxx          |
|15   |x.xxxx          |x.xxxx          |
|16   |x.xxxx          |x.xxxx          |
|17   |x.xxxx          |x.xxxx          |
|18   |x.xxxx          |x.xxxx          |
|19   |x.xxxx          |x.xxxx          |
|20   |x.xxxx          |x.xxxx          |
|21   |x.xxxx          |x.xxxx          |
|22   |x.xxxx          |x.xxxx          |
|23   |x.xxxx          |x.xxxx          |
|24   |x.xxxx          |x.xxxx          |
|25   |x.xxxx          |x.xxxx          |
