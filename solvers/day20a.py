# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    parsed_instructions = list(map(parse_line, instructions))
    closest = min(parsed_instructions, key=lambda x: abs(x["ax"]) + abs(x["ay"]) + abs(x["az"]))
    return parsed_instructions.index(closest)

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
        self.assertEqual(solve("p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>\np=<4,0,0>, v=<0,0,0>, a=<-2,0,0>\n"), 0)
