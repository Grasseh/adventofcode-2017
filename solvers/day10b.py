# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    lengths = list(fn_input[:-1])
    lengths = list(map(ord, lengths))
    lengths.append(17)
    lengths.append(31)
    lengths.append(73)
    lengths.append(47)
    lengths.append(23)
    s_hash = sparse_hash(lengths, 256, 64)
    d_hash = dense_hash(s_hash)
    return ''.join(hex_hash(d_hash))

def sparse_hash(lengths, size, rounds):
    hash_list = []
    for i in range(0, size):
        hash_list.append(i)
    position = 0
    skip = 0
    list_length = len(hash_list)
    for _whatever in range(0, rounds):
        for val in lengths:
            # Reverse
            j = position % list_length
            k = (position + val - 1) % list_length
            l_range = val // 2
            for i in range(0, l_range):
                hash_list[j], hash_list[k] = hash_list[k], hash_list[j]
                j = (j + 1) % list_length
                k = (k - 1) % list_length
            # Position
            position = (position + skip + val) % list_length
            # Skip
            skip += 1
    return hash_list

def dense_hash(previous_hash):
    d_hash = []
    for i in range(0, len(previous_hash) // 16):
        val = 0
        for j in range(0, 16):
            val = val ^ previous_hash[i * 16 + j]
        d_hash.append(val)
    return d_hash

def hex_hash(previous_hash):
    return list(map(hex_with_zero, previous_hash))

def hex_with_zero(value):
    val = hex(value)[2:]
    return val if len(val) == 2 else "0" + val

class UnitTest(unittest.TestCase):
    def test_sparse(self):
        self.assertEqual(sparse_hash([3, 4, 1, 5], 5, 1), [3, 4, 2, 1, 0])

    def test_dense(self):
        self.assertEqual(dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), [64])
    def test_hex(self):
        self.assertEqual(hex_hash([64, 7, 255]), ["40", "07", "ff"])

    def test_solve(self):
        #self.assertEqual(solve("\n"), "a2582a3a0e66e6e86e3812dcb672a272")
        self.assertEqual(solve("AoC 2017\n"), "33efeb34ea91902bb2f59c9920caa6cd")
        self.assertEqual(solve("1,2,3\n"), "3efbe78a8d82f29979031a4aa0b16a9d")
        self.assertEqual(solve("1,2,4\n"), "63960835bcdc130f0b66d7ff4f6a5a8e")
