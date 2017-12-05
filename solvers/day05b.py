# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    lines = fn_input[:-1].split("\n")
    i = 0
    steps = 0
    lines = list(map(int, lines))
    while i < len(lines):
        j = i
        i += lines[i]
        lines[j] += -1 if lines[j] >= 3 else 1
        steps += 1
    return steps

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("0\n3\n0\n1\n-3\n"), 10)
