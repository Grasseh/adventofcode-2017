# pylint: disable=missing-docstring
import unittest
import re

def solve(fn_input):
    lines = fn_input[:-1].split("\n")
    state = parse_lines(lines)
    slots = { "0" : "0" }
    current_slot = "0"
    for _ in range(int(state["totalSteps"])):
        current_instruction = state["objects"][state["currentState"]][slots[current_slot]]
        slots[current_slot] = current_instruction["write"]
        if current_instruction["move"] == "left":
            current_slot = str(int(current_slot) - 1)
        else:
            current_slot = str(int(current_slot) + 1)
        state["currentState"] = current_instruction["continue"]
        if not current_slot in slots:
            slots[current_slot] = "0"
    checksum = 0
    for key, val in slots.items():
        if val == "1":
            checksum += 1
    return checksum

def parse_lines(lines):
    regex = "Begin in state (\w+)."
    match = re.match(regex, lines[0])
    current_state = match.group(1)
    regex= "Perform a diagnostic checksum after (\w+) steps."
    match = re.match(regex, lines[1])
    nb_steps = match.group(1)
    state = {"currentState" : current_state, "totalSteps" : nb_steps, "objects" : {} }
    i = 2
    current_letter = ""
    current_state = "0"
    while i < len(lines):
        restate =    "In state (\w+):"
        revalue =    "  If the current value is (\d+):"
        rewrite =    "    - Write the value (\d+)."
        remove =     "    - Move one slot to the (\w+)."
        recontinue = "    - Continue with state (\w+)."
        matchstate = re.match(restate, lines[i])
        if matchstate:
            state["objects"][matchstate.group(1)] = {}
            current_letter = matchstate.group(1)
        matchvalue = re.match(revalue, lines[i])
        if matchvalue:
            state["objects"][current_letter][matchvalue.group(1)] = {}
            current_state = matchvalue.group(1)
        matchwrite = re.match(rewrite, lines[i])
        if matchwrite:
            state["objects"][current_letter][current_state]["write"] = matchwrite.group(1)
        matchmove = re.match(remove, lines[i])
        if matchmove:
            state["objects"][current_letter][current_state]["move"] = matchmove.group(1)
        matchcontinue = re.match(recontinue, lines[i])
        if matchcontinue:
            state["objects"][current_letter][current_state]["continue"] = matchcontinue.group(1)
        i += 1
    return state

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("Begin in state A.\nPerform a diagnostic checksum after 6 steps.\nIn state A:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state B.\n  If the current value is 1:\n    - Write the value 0.\n    - Move one slot to the left.\n    - Continue with state B.\nIn state B:\n  If the current value is 0:\n    - Write the value 1.\n    - Move one slot to the left.\n    - Continue with state A.\n  If the current value is 1:\n    - Write the value 1.\n    - Move one slot to the right.\n    - Continue with state A.\n"), 3)
