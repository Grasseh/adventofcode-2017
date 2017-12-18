# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    instructions = fn_input[:-1].split("\n")
    state_0 = {"registers" : {}, "iterator" : 0, "receiveStack" : [], "lastJump" : False, \
               "waiting" : False, "sentCount" : 0, "terminated" : False, "id" : 0}
    state_1 = {"registers" : {}, "iterator" : 0, "receiveStack" : [], "lastJump" : False, \
               "waiting" : False, "sentCount" : 0, "terminated" : False, "id" : 1}
    while True:
        #Attempt Program 1
        if not state_0["terminated"]:
            attempt_program(instructions, state_0, state_1)
        #Attempt Program 2
        if not state_1["terminated"]:
            attempt_program(instructions, state_1, state_0)
        if state_1["waiting"] and state_0["waiting"]:
            break
        if state_1["terminated"] and state_0["terminated"]:
            break
        if state_1["terminated"] and state_0["waiting"]:
            break
        if state_1["waiting"] and state_0["terminated"]:
            break
        state_1["waiting"] = False
        state_0["waiting"] = False
    return state_1["sentCount"]

def attempt_program(instructions, state, other_state):
    options = {
        "snd" : snd,
        "set" : set2, #set would be a redefinition
        "add" : add,
        "mul" : mul,
        "mod" : mod,
        "rcv" : rcv,
        "jgz" : jgz
    }
    if state["iterator"] >= len(instructions) or state["iterator"] < 0:
        return
    instruction = instructions[state["iterator"]].split()
    command = instruction[0]
    options[command](instruction, state, other_state)
    if not state["lastJump"] and not state["waiting"]:
        state["iterator"] += 1
    state["lastJump"] = False

def snd(instruction, state, other_state):
    register = get_register_value(state, instruction[1])
    other_state["receiveStack"].append(register)
    state["sentCount"] += 1

def set2(instruction, state, _):
    state["registers"][instruction[1]] = get_register_value(state, instruction[2])

def add(instruction, state, _):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] += get_register_value(state, instruction[2])

def mul(instruction, state, _):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] *= get_register_value(state, instruction[2])

def mod(instruction, state, _):
    check_register_exists(state, instruction[1])
    state["registers"][instruction[1]] = get_register_value(state, instruction[1]) % get_register_value(state, instruction[2])

def rcv(instruction, state, _):
    if len(state["receiveStack"]) > 0:
        state["registers"][instruction[1]] = state["receiveStack"].pop(0)
        return
    state["waiting"] = True

def jgz(instruction, state, _):
    if get_register_value(state, instruction[1]) > 0:
        state["iterator"] += get_register_value(state, instruction[2])
        state["lastJump"] = True

def get_register_value(state, name):
    if is_int_str(name):
        return int(name)
    check_register_exists(state, name)
    return state["registers"][name]

def check_register_exists(state, name):
    if not name in state["registers"]:
        state["registers"][name] = state["id"]

# https://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except
# WTF PYTHON
def is_int_str(s):
    return re.match(r"[-+]?\d+$", s) is not None

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("snd 1\nsnd 2\nsnd p\nrcv a\nrcv b\nrcv c\nrcv d"), 3)

    def test_input(self):
        state = {"registers" : {}}
        set2(["set", "i", "31"], state, "")
        self.assertEqual(state, {"registers" : { "i" : 31 }})
        set2(["set", "a", "1"], state, "")
        self.assertEqual(state, {"registers" : { "i" : 31, "a" : 1 }})
        state["id"] = 1
        mul(["mul", "p", "17"], state, "")
        self.assertEqual(state, {"registers" : { "i" : 31, "a" : 1, "p" : 17 }, "id" : 1})
        state["iterator"] = 3
        jgz(["jgz", "p", "p"], state, "")
        self.assertEqual(state, {"registers" : { "i" : 31, "a" : 1, "p" : 17 }, "id" : 1, "iterator" : 20, "lastJump" : True})
        jgz(["jgz", "i", "-9"], state, "")
        self.assertEqual(state, {"registers" : { "i" : 31, "a" : 1, "p" : 17 }, "id" : 1, "iterator" : 11, "lastJump" : True})
