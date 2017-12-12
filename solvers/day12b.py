# pylint: disable=missing-docstring

import unittest
import re

def solve(fn_input):
    pipes = fn_input[:-1].split("\n")
    pipes = list(map(parse_line, pipes))
    pipes = reindice(pipes)
    visited = []
    stack = []
    groups = 0
    for pipe in pipes:
        if not pipe in visited:
            groups += 1
            stack.append(pipe)
            while len(stack) > 0:
                val = stack.pop()
                if not val in visited:
                    visited.append(val)
                    for neigh in pipes[val]:
                        if not neigh in visited:
                            stack.append(neigh)
    return groups

def reindice(pipes):
    reindiced = {}
    for pipe in pipes:
        reindiced[pipe["value"]] = pipe["neighs"]
    return reindiced

def parse_line(pipe):
    string_data = re.match(r"(\d+) <-> (\d+)", pipe)
    value = string_data.group(1)
    arrow = pipe.index("<-> ")
    neigh = pipe[arrow + 4:].split(", ")
    return {"value" : value, "neighs" : neigh}

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5\n"), 2)

    def test_parse(self):
        self.assertEqual(parse_line("0 <-> 1, 4"), {"value" : "0", "neighs": ["1", "4"]})
