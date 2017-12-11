# pylint: disable=missing-docstring

import unittest
from numpy import sign

def solve(fn_input):
    moves = fn_input[:-1].split(",")
    coord_x = 0
    coord_y = 0
    for move in moves:
        if move == "s":
            coord_x -= 1
            continue
        if move == "n":
            coord_x += 1
            continue
        if move == "se":
            coord_y -= 1
            continue
        if move == "nw":
            coord_y += 1
            continue
        if move == "sw":
            coord_y += 1
            coord_x -= 1
            continue
        if move == "ne":
            coord_y -= 1
            coord_x += 1
            continue
    return hex_manhattan(coord_x, coord_y)

def hex_manhattan(x_coord, y_coord):
    if sign(x_coord) == sign(y_coord):
        return abs(x_coord + y_coord)
    return max(abs(x_coord), abs(y_coord))

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("ne,ne,ne\n"), 3)
        self.assertEqual(solve("ne,ne,sw,sw\n"), 0)
        self.assertEqual(solve("ne,ne,s,s\n"), 2)
        self.assertEqual(solve("se,sw,se,sw,sw\n"), 3)
