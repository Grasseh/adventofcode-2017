# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    components = fn_input[:-1].split("\n")
    components = list(map(lambda c: c.split("/"), components))
    best = get_best_bridge(components, [], "0")
    return best

def get_best_bridge(components, bridge, last_component):
    valid_components = list(filter(lambda x: is_valid_component(x, last_component), components))
    if len(valid_components) == 0:
        return get_bridge_score(bridge)
    best = 0
    for component in valid_components:
        bridge_copy = list(bridge)
        comp_copy = list(components)
        comp_copy.remove(component)
        bridge_copy.append(component)
        val = 0
        if component[0] != last_component or component[0] == component[1]:
            val = get_best_bridge(comp_copy, bridge_copy, component[0])
        if component[1] != last_component or component[0] == component[1]:
            val = max([val, get_best_bridge(comp_copy, bridge_copy, component[1])])
        best = max([best, val])
    return best

def is_valid_component(component, last_component):
    if last_component == "-1":
        return True
    if component[0] == last_component:
        return True
    if component[1] == last_component:
        return True

def get_bridge_score(bridge):
    score = 0
    for section in bridge:
        score += int(section[0])
        score += int(section[1])
    return score

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10\n"), 31)
