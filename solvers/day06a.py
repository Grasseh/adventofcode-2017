# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    banks = fn_input[:-1].split()
    banks = list(map(int, banks))
    store = {}
    steps = 0
    while True:
        redistribute(banks)
        steps += 1
        hash_value = generate_store_string(banks)
        if hash_value in store:
            return steps
        store[hash_value] = 1

def generate_store_string(banks):
    return ''.join(list(map(lambda x: chr(x+64), banks)))

def redistribute(banks):
    highest_bank = banks.index(max(banks))
    value_to_redistribute = banks[highest_bank]
    banks[highest_bank] = 0
    for i in range(0, value_to_redistribute):
        j = (highest_bank + i + 1) % len(banks)
        banks[j] += 1
    return banks

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("0   2   7   0\n"), 5)

    def test_generate_store_string(self):
        self.assertEqual(generate_store_string([1, 2, 3, 4]), "ABCD")
        self.assertEqual(generate_store_string([13, 20]), "MT")

    def test_redistribute(self):
        self.assertEqual(redistribute([0, 2, 7, 0]), [2, 4, 1, 2])
        self.assertEqual(redistribute([2, 4, 1, 2]), [3, 1, 2, 3])
        self.assertEqual(redistribute([3, 1, 2, 3]), [0, 2, 3, 4])
        self.assertEqual(redistribute([0, 2, 3, 4]), [1, 3, 4, 1])
        self.assertEqual(redistribute([1, 3, 4, 1]), [2, 4, 1, 2])
