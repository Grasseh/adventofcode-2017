# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    return sum(map(int, filter(str.isdigit, fn_input)))

class UnitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(solve(["1", "2"]), 3)

    def test2(self):
        self.assertEqual(solve(["1", "2", "3"]), 6)
