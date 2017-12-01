# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    input = fn_input[:-1]
    return sum(int(input[i]) for i in range(len(input)) if follows(input,i))

def follows(input, i):
    if i == len(input) - 1:
        return input[0] == input[i]
    return input[i] == input[i+1]

class UnitTest(unittest.TestCase):
    def testSolve(self):
        self.assertEqual(solve("1122\n"), 3)
    def testSolve2(self):
        self.assertEqual(solve("1111\n"), 4)
    def testSolve3(self):
        self.assertEqual(solve("1234\n"), 0)
    def testSolve4(self):
        self.assertEqual(solve("912121219\n"), 9)
