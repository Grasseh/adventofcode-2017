# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    parsed_instructions = list(map(parse_instruction, instructions))
    registers = {}
    operations = generate_operations()
    for instruction in parsed_instructions:
        if not instruction["register"] in registers:
            registers[instruction["register"]] = 0
        run_instruction = True
        if "cond_register" in instruction:
            if not instruction["cond_register"] in registers:
                registers[instruction["cond_register"]] = 0
            run_instruction = operations[instruction["cond_operator"]](registers[instruction["cond_register"]], instruction["cond_value"])
        if run_instruction:
            registers[instruction["register"]] = operations[instruction["operation"]](registers[instruction["register"]], instruction["value"])

    return max(registers.values())

def parse_instruction(inst):
    string_data = re.match(r"(\w+) (\w+) (-?\d+)", inst)
    obj = {"register" : string_data.group(1), "operation" : string_data.group(2), "value" : int(string_data.group(3))}
    string_data = re.match(r"(\w+) (\w+) (-?\d+) if (\w+) (.+) (-?\d+)", inst)
    if string_data:
        obj["cond_register"] = string_data.group(4)
        obj["cond_operator"] = string_data.group(5)
        obj["cond_value"] = int(string_data.group(6))
    return obj

def generate_operations():
    return {
        "==": (lambda x,y: x == y),
        ">" : (lambda x,y: x > y),
        ">=": (lambda x,y: x >= y),
        "<=": (lambda x,y: x <= y),
        "!=": (lambda x,y: x != y),
        "<": (lambda x,y: x < y),
        "inc": (lambda x,y: x + y),
        "dec": (lambda x,y: x - y)
    }

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("b inc 5 if a > 1\na inc 1 if b < 5\nc dec -10 if a >= 1\nc inc -20 if c == 10\n"), 1)
