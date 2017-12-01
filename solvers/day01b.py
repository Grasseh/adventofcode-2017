# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    fn_input = fn_input[:-1]
    step = len(fn_input) // 2
    return sum(int(fn_input[i]) for i in range(len(fn_input)) if follows(fn_input, i, step))

def follows(array, i, step):
    if i + step >= len(array):
        return array[i] == array[step + i - len(array)]
    return array[i] == array[i + step]

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("1212\n"), 6)
    def test_solve2(self):
        self.assertEqual(solve("1221\n"), 0)
    def test_solve3(self):
        self.assertEqual(solve("123425\n"), 4)
    def test_solve4(self):
        self.assertEqual(solve("123123\n"), 12)
    def test_solve5(self):
        self.assertEqual(solve("12131415\n"), 4)
