# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    lengths = fn_input[:-1].split(",")
    lengths = list(map(int, lengths))
    solution = solve_with_size(lengths, 256)
    return solution[0] * solution[1]

def solve_with_size(lengths, size):
    hash_list = []
    for i in range(0, size):
        hash_list.append(i)
    position = 0
    skip = 0
    list_length = len(hash_list)
    for val in lengths:
        # Reverse
        j = position
        k = (position + val - 1) % list_length
        l = val // 2
        for i in range(0, l):
            hash_list[j], hash_list[k] = hash_list[k], hash_list[j]
            j = (j + 1) % list_length
            k = (k - 1) % list_length
        # Position
        position = (position + skip + val) % list_length
        # Skip
        skip += 1
    return hash_list

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve_with_size([3, 4, 1, 5], 5), [3, 4, 2, 1, 0])
