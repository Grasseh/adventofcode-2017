# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    base = (fn_input[:-1])
    groups = []
    for i in range(0, 128):
        hashed = binary_line(knot_hash(base + "-" + str(i)))
        groups.append(hashed)
    visited = []
    stack = []
    answer = 0
    for row in range(0, 128):
        for col in range(0, 128):
            name = str(row).zfill(3) + str(col).zfill(3)
            if not name in visited:
                if groups[row][col] != "1":
                    visited.append(name)
                    continue
                answer += 1
                stack.append(name)
                while len(stack) > 0:
                    val = stack.pop()
                    if not val in visited:
                        visited.append(val)
                        for neigh in generate_neighbors(val):
                            if not neigh in visited:
                                if groups[int(neigh[:3])][int(neigh[-3:])] == "1":
                                    stack.append(neigh)
    return answer

def knot_hash(fn_input):
    lengths = list(fn_input)
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

def binary_line(hex_val):
    return bin(int(hex_val, 16))[2:].zfill(128)

def generate_neighbors(val):
    col = int(val[:3])
    row = int(val[-3:])
    ret_value = []
    if col < 127:
        ret_value.append(str(col + 1).zfill(3) + str(row).zfill(3))
    if row < 127:
        ret_value.append(str(col).zfill(3) + str(row + 1).zfill(3))
    if col > 0:
        ret_value.append(str(col - 1).zfill(3) + str(row).zfill(3))
    if row > 0:
        ret_value.append(str(col).zfill(3) + str(row - 1).zfill(3))
    return ret_value


class UnitTest(unittest.TestCase):
    def test_sparse(self):
        self.assertEqual(sparse_hash([3, 4, 1, 5], 5, 1), [3, 4, 2, 1, 0])

    def test_solve(self):
        self.assertEqual(solve("flqrgnkx\n"), 1242)

    def test_dense(self):
        self.assertEqual(dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]), [64])

    def test_hex(self):
        self.assertEqual(hex_hash([64, 7, 255]), ["40", "07", "ff"])

    def test_binary(self):
        self.assertEqual(binary_line("a0c20170000000000000000000000000").index("1010000011000010000000010111"), 0)

    def test_gen_neigh(self):
        self.assertEqual(generate_neighbors("001000"), ["002000", "001001", "000000"])
        self.assertEqual(generate_neighbors("045100"), ["046100", "045101", "044100", "045099"])

    def test_knot(self):
        self.assertEqual(knot_hash("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
        self.assertEqual(knot_hash("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
        self.assertEqual(knot_hash("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")
