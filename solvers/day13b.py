# pylint: disable=missing-docstring

import unittest

def solve(fn_input):
    scanners = fn_input[:-1].split("\n")
    caught = True
    frame = 0
    while caught:
        caught = False
        for scanner in scanners:
            split = scanner.split()
            layer = int(split[0][:-1])
            depth = int(split[1])
            if is_caught(layer, depth, frame):
                frame += 1
                caught = True
                break
    return frame

def is_caught(layer, depth, frame):
    return (layer + frame) % ((depth - 1) * 2) == 0

class UnitTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("0: 3\n1: 2\n4: 4\n6: 4\n"), 10)
