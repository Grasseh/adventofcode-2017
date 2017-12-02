# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    lines = fn_input[:-1].split("\n")
    return sum(get_largest_difference(parse_line(line)) for line in lines)

def parse_line(line):
    return list(map(int, re.split(r'\W+', line)))

def get_largest_difference(line):
    return max(line) - min(line)

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("5 1 9 5\n7 5 3\n2 4 6 8\n"), 18)
