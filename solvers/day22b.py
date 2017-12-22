# pylint: disable=missing-docstring
import unittest
import numpy

INFECTED = 1
FLAGGED = 2
WEAKENED = 3
CLEANED = 0

def solve(fn_input, iterations=10000000):
    instructions = fn_input[:-1].split("\n")
    right_values = {"n" : "e", "e" : "s", "s" : "w", "w" : "n"}
    left_values = {"n" : "w", "e" : "n", "s" : "e", "w" : "s"}
    opp_values = {"n" : "s", "e" : "w", "s" : "n", "w" : "e"}
    grid = numpy.zeros((10001, 10001))
    for i, line in enumerate(instructions):
        for j, char in enumerate(line):
            if char == "#":
                grid[5000+j][5000+i] = INFECTED
    x = 5000 + len(instructions) // 2
    y = x
    direction = "n"
    infection_count = 0
    for i in range(iterations):
        if grid[x][y] == INFECTED:
            grid[x][y] = FLAGGED
            direction = right_values[direction]
        elif grid[x][y] == FLAGGED:
            grid[x][y] = CLEANED
            direction = opp_values[direction]
        elif grid[x][y] == WEAKENED:
            grid[x][y] = INFECTED
            infection_count += 1
        else:
            grid[x][y] = WEAKENED
            direction = left_values[direction]
        if(direction == "n"):
            y -= 1
        if(direction == "s"):
            y += 1
        if(direction == "w"):
            x -= 1
        if(direction == "e"):
            x += 1
    return infection_count

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("..#\n#..\n...\n", 100), 26)
        self.assertEqual(solve("..#\n#..\n...\n"), 2511944)
