# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    parsed_instructions = list(map(parse_line, instructions))
    for _ in range(0, 40):
        #Simulate
        for instruction in parsed_instructions:
            instruction["vx"] += instruction["ax"]
            instruction["vy"] += instruction["ay"]
            instruction["vz"] += instruction["az"]
            instruction["px"] += instruction["vx"]
            instruction["py"] += instruction["vy"]
            instruction["pz"] += instruction["vz"]
        #Check Collisions
        non_collision = []
        to_remove = []
        for instruction in parsed_instructions:
            coll = False
            for other_instruction in non_collision:
                if instruction["px"] == other_instruction["px"] and \
                   instruction["py"] == other_instruction["py"] and \
                   instruction["pz"] == other_instruction["pz"]:
                    to_remove.append(other_instruction)
                    coll = True
            if not coll:
                non_collision.append(instruction)
        for remove in to_remove:
            if remove in non_collision:
                non_collision.remove(remove)
        parsed_instructions = non_collision
    return len(parsed_instructions)

def parse_line(line):
    value = {}
    expr = "p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>"
    string_data = re.match(expr, line)
    if string_data:
        value["px"] = int(string_data.group(1))
        value["py"] = int(string_data.group(2))
        value["pz"] = int(string_data.group(3))
        value["vx"] = int(string_data.group(4))
        value["vy"] = int(string_data.group(5))
        value["vz"] = int(string_data.group(6))
        value["ax"] = int(string_data.group(7))
        value["ay"] = int(string_data.group(8))
        value["az"] = int(string_data.group(9))
    return value

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>\np=<-4,0,0>, v=<2,0,0>, a=<0,0,0>\n"), 0)
