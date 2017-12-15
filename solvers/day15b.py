# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    starts = (fn_input[:-1].split("\n"))
    gen_a = int(starts[0])
    gen_b = int(starts[1])
    count = 0
    stack_a = []
    stack_b = []
    while len(stack_b) < 5000000:
        gen_a = gen_a * 16807 % 2147483647
        gen_b = gen_b * 48271 % 2147483647
        if gen_a % 4 == 0:
            stack_a.append(gen_a)
        if gen_b % 8 == 0:
            stack_b.append(gen_b)
    a_count = len(stack_a)
    b_count = len(stack_b)
    for i in range(0, min([a_count, b_count])):
        count += 1 if judge(stack_a[i], stack_b[i]) else 0
    return count

def judge(gen_a, gen_b):
    return bin(gen_a)[-16:].zfill(18) == bin(gen_b)[-16:].zfill(18)

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("65\n8921\n"), 309)
