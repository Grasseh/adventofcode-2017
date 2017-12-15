# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    starts = (fn_input[:-1].split("\n"))
    gen_a = int(starts[0])
    gen_b = int(starts[1])
    count = 0
    for _we in range(0, 40000000):
        gen_a = gen_a * 16807 % 2147483647
        gen_b = gen_b * 48271 % 2147483647
        count += 1 if judge(gen_a, gen_b) else 0
    return count

def judge(gen_a, gen_b):
    return bin(gen_a)[-16:].zfill(18) == bin(gen_b)[-16:].zfill(18)

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("65\n8921\n"), 588)
