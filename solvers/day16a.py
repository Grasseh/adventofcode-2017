# pylint: disable=missing-docstring
import unittest
from functools import reduce
from numpy import roll

def solve(fn_input):
    moves = (fn_input[:-1].split(","))
    dance_line = ["a", "b", "c", "d", \
                    "e", "f", "g", "h", \
                    "i", "j", "k", "l", \
                    "m", "n", "o", "p"]
    return solve_with_line(moves, dance_line)

def solve_with_line(moves, dance_line):
    options = {
        "s" : spin,
        "x" : exchange,
        "p" : pair
    }
    for move in moves:
        dance_line = options[move[:1]](dance_line, move)
    return "".join(dance_line)

def spin(positions, move):
    shift = int(move[1:])
    return roll(positions, shift).tolist()

def exchange(positions, move):
    vals = list(map(int, move[1:].split("/")))
    positions[vals[0]], positions[vals[1]] = \
            positions[vals[1]], positions[vals[0]]
    return positions

def pair(positions, move):
    vals = move[1:].split("/")
    for i in range(0, len(positions)):
        if positions[i] == vals[0]:
            positions[i] = vals[1]
            continue
        if positions[i] == vals[1]:
            positions[i] = vals[0]
    return positions

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve_with_line(["s1", "x3/4", "pe/b"], \
                                         ["a", "b", "c", "d", "e"]), "baedc")

    def test_spin(self):
        self.assertEqual(spin(["a", "b", "c", "d", "e"], "s2"), \
                                  ["d", "e", "a", "b", "c"])

    def test_exchange(self):
        self.assertEqual(exchange(["a", "b", "c", "d", "e"], "x2/3"), \
                                  ["a", "b", "d", "c", "e"])

    def test_pair(self):
        self.assertEqual(pair(["a", "b", "c", "d", "e"], "pe/b"), \
                                  ["a", "e", "c", "d", "b"])
