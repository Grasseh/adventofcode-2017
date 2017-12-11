# pylint: disable=missing-docstring

import unittest
from numpy import sign

def solve(fn_input):
    moves = fn_input[:-1].split(",")
    coord_x = 0
    coord_y = 0
    furthest = 0
    for move in moves:
        if move == "s":
            coord_x -= 1
        if move == "n":
            coord_x += 1
        if move == "se":
            coord_y -= 1
        if move == "nw":
            coord_y += 1
        if move == "sw":
            coord_y += 1
            coord_x -= 1
        if move == "ne":
            coord_y -= 1
            coord_x += 1
        distance = hex_manhattan(coord_x, coord_y)
        furthest = distance if furthest < distance else furthest
    return furthest

def hex_manhattan(x_coord, y_coord):
    if sign(x_coord) == sign(y_coord):
        return abs(x_coord + y_coord)
    return max(abs(x_coord), abs(y_coord))

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("ne,ne,ne\n"), 3)
        self.assertEqual(solve("ne,ne,sw,sw\n"), 2)
