# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    instructions = fn_input[:-1]
    points = 0
    is_cancelled = False
    in_garbage = False
    for char in instructions:
        if is_cancelled:
            is_cancelled = False
            continue
        if in_garbage:
            if char == ">":
                in_garbage = False
                continue
            if char == "!":
                is_cancelled = True
                continue
            points += 1
            continue
        if char == "<":
            in_garbage = True
            continue
    return points

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("<>\n"), 0)
        self.assertEqual(solve("<random characters>\n"), 17)
        self.assertEqual(solve("<<<<>\n"), 3)
        self.assertEqual(solve("<{!>}>\n"), 2)
        self.assertEqual(solve("<!!>\n"), 0)
        self.assertEqual(solve("<!!!>>\n"), 0)
        self.assertEqual(solve('<{o"i!a,<{i<a>\n'), 10)
