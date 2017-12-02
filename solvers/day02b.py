# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    lines = fn_input[:-1].split("\n")
    return sum(get_division(parse_line(line)) for line in lines)

def parse_line(line):
    return list(map(int, re.split(r'\W+', line)))

def get_division(line):
    for i in range(0, len(line)):
        for j in range(i+1, len(line)):
            if line[i] % line[j] == 0:
                return line[i] // line[j]
            if line[j] % line[i] == 0:
                return line[j] // line[i]

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("5 9 2 8\n9 4 7 3\n3 8 6 5\n"), 9)
