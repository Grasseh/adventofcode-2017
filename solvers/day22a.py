# pylint: disable=missing-docstring
import unittest

def solve(fn_input, iterations=10000):
    instructions = fn_input[:-1].split("\n")
    right_values = {"n" : "e", "e" : "s", "s" : "w", "w" : "n"}
    left_values = {"n" : "w", "e" : "n", "s" : "e", "w" : "s"}
    infected_list = []
    for i, line in enumerate(instructions):
        for j, char in enumerate(line):
            if char == "#":
                infected_list.append([j, i])
    x = len(instructions) // 2
    y = x
    direction = "n"
    infection_count = 0
    for _ in range(iterations):
        if [x, y] in infected_list:
            infected_list.remove([x, y])
            direction = right_values[direction]
        else:
            infected_list.append([x, y])
            direction = left_values[direction]
            infection_count += 1
        if(direction == "n"):
            y -= 1
        if(direction == "s"):
            y += 1
        if(direction == "w"):
            x -= 1
        if(direction == "e"):
            x += 1
    return infection_count

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("..#\n#..\n...\n", 7), 5)
        self.assertEqual(solve("..#\n#..\n...\n", 70), 41)
        self.assertEqual(solve("..#\n#..\n...\n"), 5587)
