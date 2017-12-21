# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input, iterations=5):
    instructions = fn_input[:-1].split("\n")
    rules = list(map(parse_line, instructions))
    grid = [2, 1, 7]
    for _ in range(iterations):
        is_two_d = len(grid) % 2 == 0
        splits = []
        if is_two_d:
            splits = split_two_d(grid)
        else:
            splits = split_three_d(grid)
        splits = transform_splits(splits, rules, is_two_d)
        grid = merge_splits(splits, 3 if is_two_d else 4)
    for row in grid:
        print(bin(row)[2:].zfill(18))
    return bits_open(grid)

def split_two_d(grid):
    splits = []
    size = len(grid) // 2
    for i in range(size):
        arr = []
        for j in range(size):
            a = grid[i*2] >> j * 2 & 3
            b = grid[i*2+1] >> j * 2 & 3
            arr.insert(0, [a, b])
        splits.append(arr)
    return splits

def split_three_d(grid):
    splits = []
    size = len(grid) // 3
    for i in range(size):
        arr = []
        for j in range(size):
            a = grid[i*3] >> j * 3 & 7
            b = grid[i*3+1] >> j * 3 & 7
            c = grid[i*3+2] >> j * 3 & 7
            arr.insert(0, [a, b, c])
        splits.append(arr)
    return splits

def transform_splits(splits, rules, is_two_d):
    transformed = []
    dim = 2 if is_two_d else 3
    for split in splits:
        subarr = []
        for sub_split in split:
            for rule in rules:
                if rule[0] != dim:
                    continue
                if split_is(sub_split, rule[1]):
                    subarr.append(rule[2])
                    break
        transformed.append(subarr)
    return transformed

def split_is(split, rule):
    if split == rule:
        return True
    r90 = rotate90(split)
    r180 = rotate180(split)
    r270 = rotate270(split)
    reverse = list(reversed(split))
    rr90 = list(reversed(r90))
    rr180 = list(reversed(r180))
    rr270 = list(reversed(r270))
    return r90 == rule or r180 == rule or r270 == rule or reverse == rule or rr90 == rule or rr180 == rule or rr270 == rule

def rotate90(split):
    div = len(split)
    rotated = []
    if(div == 2):
        rotated.append((2 if split[1] & 2 else 0) + (1 if split[0] & 2 else 0))   
        rotated.append((2 if split[1] & 1 else 0) + (1 if split[0] & 1 else 0))   
    if(div == 3):
        rotated.append((4 if split[2] & 4 else 0) + (2 if split[1] & 4 else 0) + (1 if split[0] & 4 else 0))   
        rotated.append((4 if split[2] & 2 else 0) + (2 if split[1] & 2 else 0) + (1 if split[0] & 2 else 0))   
        rotated.append((4 if split[2] & 1 else 0) + (2 if split[1] & 1 else 0) + (1 if split[0] & 1 else 0))   
    return rotated

def rotate270(split):
    div = len(split)
    rotated = []
    if(div == 2):
        rotated.append((2 if split[0] & 1 else 0) + (1 if split[1] & 1 else 0))   
        rotated.append((2 if split[0] & 2 else 0) + (1 if split[1] & 2 else 0))   
    if(div == 3):
        rotated.append((4 if split[0] & 1 else 0) + (2 if split[1] & 1 else 0) + (1 if split[2] & 1 else 0))   
        rotated.append((4 if split[0] & 2 else 0) + (2 if split[1] & 2 else 0) + (1 if split[2] & 2 else 0))   
        rotated.append((4 if split[0] & 4 else 0) + (2 if split[1] & 4 else 0) + (1 if split[2] & 4 else 0))   
    return rotated

def rotate180(split):
    div = len(split)
    rotated = []
    if(div == 2):
        rotated.append((2 if split[1] & 1 else 0) + (1 if split[1] & 2 else 0))   
        rotated.append((2 if split[0] & 1 else 0) + (1 if split[0] & 2 else 0))   
    if(div == 3):
        rotated.append((4 if split[2] & 1 else 0) + (2 if split[2] & 2 else 0) + (1 if split[2] & 4 else 0))   
        rotated.append((4 if split[1] & 1 else 0) + (2 if split[1] & 2 else 0) + (1 if split[1] & 4 else 0))   
        rotated.append((4 if split[0] & 1 else 0) + (2 if split[0] & 2 else 0) + (1 if split[0] & 4 else 0))   
    return rotated

def merge_splits(splits, amount=3):
    grid = []
    for split in splits:
        for i in range(len(split[0])):
            val = 0
            for j in range(len(split)):
                val += split[j][i] << j * amount
            grid.append(val)
    return grid

def bits_open(grid):
    return sum(str(bin(i))[2:].count("1") for i in grid)

def parse_line(line):
    value = []
    two_expr = "(.)(.)/(.)(.) => (.)(.)(.)/(.)(.)(.)/(.)(.)(.)"
    three_expr = "(.)(.)(.)/(.)(.)(.)/(.)(.)(.) => (.)(.)(.)(.)/(.)(.)(.)(.)/(.)(.)(.)(.)/(.)(.)(.)(.)"
    string_data = re.match(two_expr, line)
    if string_data:
        value.append(2)
        two_d_arr = []
        two_d_arr.append((2 if string_data.group(1) == "#" else 0) + (1 if string_data.group(2) == "#" else 0))
        two_d_arr.append((2 if string_data.group(3) == "#" else 0) + (1 if string_data.group(4) == "#" else 0))
        value.append(two_d_arr)
        three_d_arr = []
        three_d_arr.append((4 if string_data.group(5) == "#" else 0) + (2 if string_data.group(6) == "#" else 0) + \
                         (1 if string_data.group(7) == "#" else 0))
        three_d_arr.append((4 if string_data.group(8) == "#" else 0) + (2 if string_data.group(9) == "#" else 0) + \
                         (1 if string_data.group(10) == "#" else 0))
        three_d_arr.append((4 if string_data.group(11) == "#" else 0) + (2 if string_data.group(12) == "#" else 0) + \
                         (1 if string_data.group(13) == "#" else 0))
        value.append(three_d_arr)
    string_data = re.match(three_expr, line)
    if string_data:
        value.append(3)
        three_d_arr = []
        three_d_arr.append((4 if string_data.group(1) == "#" else 0) + (2 if string_data.group(2) == "#" else 0) + \
                         (1 if string_data.group(3) == "#" else 0))
        three_d_arr.append((4 if string_data.group(4) == "#" else 0) + (2 if string_data.group(5) == "#" else 0) + \
                         (1 if string_data.group(6) == "#" else 0))
        three_d_arr.append((4 if string_data.group(7) == "#" else 0) + (2 if string_data.group(8) == "#" else 0) + \
                         (1 if string_data.group(9) == "#" else 0))
        value.append(three_d_arr)
        four_d_arr = []
        four_d_arr.append((8 if string_data.group(10) == "#" else 0) + (4 if string_data.group(11) == "#" else 0) + \
                         (2 if string_data.group(12) == "#" else 0) + (1 if string_data.group(13) == "#" else 0))
        four_d_arr.append((8 if string_data.group(14) == "#" else 0) + (4 if string_data.group(15) == "#" else 0) + \
                         (2 if string_data.group(16) == "#" else 0) + (1 if string_data.group(17) == "#" else 0))
        four_d_arr.append((8 if string_data.group(18) == "#" else 0) + (4 if string_data.group(19) == "#" else 0) + \
                         (2 if string_data.group(20) == "#" else 0) + (1 if string_data.group(21) == "#" else 0))
        four_d_arr.append((8 if string_data.group(22) == "#" else 0) + (4 if string_data.group(23) == "#" else 0) + \
                         (2 if string_data.group(24) == "#" else 0) + (1 if string_data.group(25) == "#" else 0))
        value.append(four_d_arr)
    return value

class UnitTest(unittest.TestCase):
    def test_parse_line(self):
        self.assertEqual(parse_line("../.# => ##./#../..."), [2, [0, 1], [6, 4, 0]])
        self.assertEqual(parse_line(".#./..#/### => #..#/..../..../#..#"), [3, [2, 1, 7], [9, 0, 0, 9]])

    def test_solve(self):
        self.assertEqual(solve("../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#\n", 2), 12)

    def test_bits_open(self):
        self.assertEqual(bits_open([2+4+16+32, 4+32, 0, 2+4+16+32, 4+32, 0]), 12)

    def test_split_two(self):
        self.assertEqual(split_two_d([9, 0, 0, 9]), [[[2,0], [1,0]], [[0,2], [0, 1]]])

    def test_split_three(self):
        self.assertEqual(split_three_d([325, 144, 144, 257, 80, 1, 256, 144, 68]), [[[5, 2, 2], [0, 2, 2], [5, 0, 0]], \
                                                                                   [[4, 1, 0], [0, 2, 0], [1, 0, 1]], \
                                                                                   [[4, 2, 1], [0, 2, 0], [0, 0, 4]]]) 

    def test_transfrom_splits(self):
        rules = [[2, [0, 1], [6, 4, 0]]]
        self.assertEqual(transform_splits([[[2,0], [1,0]], [[0,2], [0, 1]]], rules, True), [[[6, 4, 0], [6, 4, 0]], [[6, 4, 0], [6, 4, 0]]])

    def test_merge_two(self):
        self.assertEqual(merge_splits([[[6, 4, 0], [6, 4, 0]], [[6, 4, 0], [6, 4, 0]]]), [54, 36, 0, 54, 36, 0])

    def test_rotate_90(self):
        self.assertEqual(rotate90([1, 0]), [0, 1])

    def test_rotate_180(self):
        self.assertEqual(rotate180([2, 0]), [0, 1])

    def test_rotate_270(self):
        self.assertEqual(rotate270([0, 2]), [0, 1])
