# pylint: disable=missing-docstring
import unittest
from numpy import roll

def solve(fn_input):
    jump = int(fn_input[:-1])
    return solve_with_length(jump, 2017)

def solve_with_length(jump, rotations):
    arr = [0]
    position = 0
    for i in range(1, rotations + 1):
        position = (position + jump) % (i) + 1
        arr.insert(position, i)
    return arr[(position + 1) % len(arr)]

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve_with_length(3, 0), 0)
        self.assertEqual(solve_with_length(3, 1), 0)
        self.assertEqual(solve_with_length(3, 2), 1)
        self.assertEqual(solve_with_length(3, 3), 1)
        self.assertEqual(solve_with_length(3, 4), 3)
        self.assertEqual(solve_with_length(3, 5), 2)
        self.assertEqual(solve_with_length(3, 6), 1)
        self.assertEqual(solve_with_length(3, 7), 2)
        self.assertEqual(solve_with_length(3, 8), 6)
        self.assertEqual(solve_with_length(3, 9), 5)
        self.assertEqual(solve_with_length(3, 2017), 638)
