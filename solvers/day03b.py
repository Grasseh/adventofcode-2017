# pylint: disable=missing-docstring
import unittest
import numpy
numpy.set_printoptions(threshold=numpy.inf)

def solve(fn_input):
    number = int(fn_input[:-1])
    grid = numpy.zeros((21, 21))
    i = 11
    j = 11
    grid[i][j] = 1
    move_max = 1
    current_move = 0
    direction = "E"
    while True:
        current_move += 1
        if direction == "E":
            if current_move == move_max:
                current_move = 0
                direction = "N"
            j += 1
        elif direction == "N":
            if current_move == move_max:
                current_move = 0
                move_max += 1
                direction = "W"
            i += 1
        elif direction == "W":
            if current_move == move_max:
                current_move = 0
                direction = "S"
            j -= 1
        elif direction == "S":
            if current_move == move_max:
                move_max += 1
                current_move = 0
                direction = "E"
            i -= 1
        set_grid_value(grid, i, j)
        if grid[i][j] > number:
            return grid[i][j]

def set_grid_value(grid, i, j):
    grid[i][j] = grid[i+1][j] + grid[i+1][j-1] + grid[i+1][j+1] + grid[i][j+1] + \
                 grid[i-1][j] + grid[i-1][j-1] + grid[i-1][j+1] + grid[i][j-1]

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("1\n"), 2)
        self.assertEqual(solve("8\n"), 10)
        self.assertEqual(solve("312\n"), 330)
        self.assertEqual(solve("600\n"), 747)
