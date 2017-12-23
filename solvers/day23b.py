# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    state = {"registers" : {"a" : 1}, "iterator" : 0, "lastJump" : False, "mulCount" : 0}
    options = {
        "set" : set2,
        "sub" : sub,
        "mul" : mul,
        "jnz" : jnz
    }
    for i in range(8):
        instruction = instructions[state["iterator"]].split()
        command = instruction[0]
        options[command](instruction, state)
        if not state["lastJump"]:
            state["iterator"] += 1
        state["lastJump"] = False

    h = 0
    b = state["registers"]["b"]
    while b <= state["registers"]["c"]:
        f = 1
        d = 2
        for d in range(2, b):
            for e in range(2, b):
                val = d * e
                if(val == b):
                    f = 0
                if(val >= b):
                    break
            if f == 0:
                break
        if f == 0:
            h += 1
        b += 17
    return h

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
        self.assertEqual(solve("set b 3\nset c b\njnz a 2\njnz 1 5\nmul b 2\nsub b -4\nset c b\nsub c -68\nset h 1\n"), 4) #between 10 and 78 --> 10, 27, 44, 61, 78
