# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    #width = len(instructions[0])
    #height = len(instructions)
    y = 0
    x = instructions[0].index("|")
    done = False
    count = 0
    direction = "S"
    collection = ""
    while not done:
        if direction == "S":
            y += 1
        if direction == "N":
            y -= 1
        if direction == "E":
            x += 1
        if direction == "W":
            x -= 1
        count += 1
        if instructions[y][x] == "|" or instructions[y][x] == "-":
            continue
        if instructions[y][x] == "+":
            direction = change_direction(direction, x, y, instructions)
            continue
        if instructions[y][x] != " ":
            continue
        return count

def change_direction(direction, x, y, instructions):
    if direction != "S" and instructions[y-1][x] != " ":
        return "N"
    if direction != "N" and instructions[y+1][x] != " ":
        return "S"
    if direction != "W" and instructions[y][x+1] != " ":
        return "E"
    if direction != "E" and instructions[y][x-1] != " ":
        return "W"


class UnitTest(unittest.TestCase):
    def test_solve(self):
        input_str  = "     |          \n"
        input_str += "     |  +--+    \n"
        input_str += "     A  |  C    \n"
        input_str += " F---|----E|--+ \n"
        input_str += "     |  |  |  D \n"
        input_str += "     +B-+  +--+ \n"
        input_str += "                \n"
        self.assertEqual(solve(input_str), 38)
