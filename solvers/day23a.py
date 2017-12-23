# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    state = {"registers" : {}, "iterator" : 0, "lastJump" : False, "mulCount" : 0}
    options = {
        "set" : set2,
        "sub" : sub,
        "mul" : mul,
        "jnz" : jnz
    }
    while True:
        if state["iterator"] >= len(instructions) or state["iterator"] < 0:
            return state["mulCount"]
        instruction = instructions[state["iterator"]].split()
        command = instruction[0]
        options[command](instruction, state)
        if not state["lastJump"]:
            state["iterator"] += 1
        state["lastJump"] = False

def set2(instruction, state):
    state["registers"][instruction[1]] = get_register_value(state, instruction[2])

def sub(instruction, state):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] -= get_register_value(state, instruction[2])

def mul(instruction, state):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] *= get_register_value(state, instruction[2])
    state["mulCount"] += 1

def jnz(instruction, state):
    if get_register_value(state, instruction[1]) != 0:
        state["iterator"] += get_register_value(state, instruction[2])
        state["lastJump"] += True

def get_register_value(state, name):
    if is_int_str(name):
        return int(name)
    check_register_exists(state, name)
    return state["registers"][name]

def check_register_exists(state, name):
    if not name in state["registers"]:
        state["registers"][name] = 0

# https://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
# WTF PYTHON
def is_int_str(s):
    return re.match(r"[-+]?\d+$", s) is not None

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("set a 1\nsub a 2\njnz 1 a\nmul a 5\nsub a 2"), 0)
