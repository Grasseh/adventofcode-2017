# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    jump = int(fn_input[:-1])
    return solve_with_length(jump, 50000000)

def solve_with_length(jump, rotations):
    position = 0
    high = 0
    for i in range(1, rotations + 1):
        position = (position + jump) % (i) + 1
        high = i if position == 1 else high
    return high

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve_with_length(3, 0), 0)
        self.assertEqual(solve_with_length(3, 1), 1)
        self.assertEqual(solve_with_length(3, 2), 2)
        self.assertEqual(solve_with_length(3, 3), 2)
        self.assertEqual(solve_with_length(3, 4), 2)
        self.assertEqual(solve_with_length(3, 5), 5)
        self.assertEqual(solve_with_length(3, 6), 5)
        self.assertEqual(solve_with_length(3, 7), 5)
        self.assertEqual(solve_with_length(3, 8), 5)
        self.assertEqual(solve_with_length(3, 9), 9)
