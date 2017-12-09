# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    instructions = fn_input[:-1]
    points = 0
    depth = 0
    in_garbage = False
    is_cancelled = False
    for char in instructions:
        if is_cancelled:
            is_cancelled = False
            continue
        if in_garbage:
            if char == ">":
                in_garbage = False
            if char == "!":
                is_cancelled = True
            continue
        if char == "<":
            in_garbage = True
            continue
        if char == "{":
            depth += 1
            points += depth
            continue
        if char == "}":
            depth -= 1
    return points

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("{}\n"), 1)
        self.assertEqual(solve("{{{}}}\n"), 6)
        self.assertEqual(solve("{{},{}}\n"), 5)
        self.assertEqual(solve("{{{},{},{{}}}}\n"), 16)
        self.assertEqual(solve("{<a>,<a>,<a>,<a>}\n"), 1)
        self.assertEqual(solve("{{<ab>},{<ab>},{<ab>},{<ab>}}\n"), 9)
        self.assertEqual(solve("{{<!!>},{<!!>},{<!!>},{<!!>}}\n"), 9)
        self.assertEqual(solve("{{<a!>},{<a!>},{<a!>},{<ab>}}\n"), 3)
