# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    components = fn_input[:-1].split("\n")
    components = list(map(lambda c: c.split("/"), components))
    best = get_best_bridge(components, [], "0")
    return get_bridge_score(best)

def get_best_bridge(components, bridge, last_component):
    valid_components = list(filter(lambda x: is_valid_component(x, last_component), components))
    if len(valid_components) == 0:
        return bridge
    best = 0
    best_bridge = []
    for component in valid_components:
        bridge_copy = list(bridge)
        comp_copy = list(components)
        comp_copy.remove(component)
        bridge_copy.append(component)
        bridge_0 = []
        bridge_1 = []
        local_best = []
        if component[0] != last_component or component[0] == component[1]:
            bridge_0 = get_best_bridge(comp_copy, bridge_copy, component[0])
        if component[1] != last_component or component[0] == component[1]:
            bridge_1 = get_best_bridge(comp_copy, bridge_copy, component[1])
        bridge_0 = compare_bridge(bridge_0, bridge_1)
        best_bridge = compare_bridge(bridge_0, best_bridge)
    return best_bridge

def compare_bridge(bridge_0, bridge_1):
    if len(bridge_0) > len(bridge_1):
        local_best = bridge_0
    elif len(bridge_1) > len(bridge_0):
        local_best = bridge_1
    else:
        if(get_bridge_score(bridge_0) > get_bridge_score(bridge_1)):
            local_best = bridge_0
        else:
            local_best = bridge_1
    return local_best

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
        self.assertEqual(solve("0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10\n"), 19)
