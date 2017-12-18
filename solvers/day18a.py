# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    state = {"lastSound" : 0, "registers" : {}, "iterator" : 0, "lastRecover" : 0, "lastJump" : False}
    options = {
        "snd" : snd,
        "set" : set2,
        "add" : add,
        "mul" : mul,
        "mod" : mod,
        "rcv" : rcv,
        "jgz" : jgz
    }
    while True:
        if state["iterator"] >= len(instructions) or state["iterator"] < 0:
            return
        instruction = instructions[state["iterator"]].split()
        command = instruction[0]
        options[command](instruction, state)
        if state["lastRecover"] != 0:
            return state["lastRecover"]
        if not state["lastJump"]:
            state["iterator"] += 1
        state["lastJump"] = False

def snd(instruction, state):
    register = get_register_value(state, instruction[1])
    state["lastSound"] = register

def set2(instruction, state):
    state["registers"][instruction[1]] = get_register_value(state, instruction[2])

def add(instruction, state):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] += get_register_value(state, instruction[2])

def mul(instruction, state):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] *= get_register_value(state, instruction[2])

def mod(instruction, state):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] = get_register_value(state, instruction[1]) % get_register_value(state, instruction[2])

def rcv(instruction, state):
    if get_register_value(state, instruction[1]) != 0:
        state["registers"][instruction[1]] = state["lastSound"]
        state["lastRecover"] = state["lastSound"]

def jgz(instruction, state):
    if get_register_value(state, instruction[1]) > 0:
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
        self.assertEqual(solve("set a 1\nadd a 2\nmul a a\nmod a 5\nsnd a\nset a 0\nrcv a\njgz a -1\nset a 1\njgz a -2\n"), 4)
