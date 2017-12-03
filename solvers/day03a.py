# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    number = int(fn_input[:-1])
    ring_number = get_ring_number(number)
    ring_centers = get_ring_centers(ring_number)
    get_closest = get_closest_distance(number)
    distance_to_center = min(map(get_closest, ring_centers))
    return distance_to_center + ring_number

def get_closest_distance(vala):
    return lambda b: abs(vala-b)

def get_ring_number(number):
    i = 0
    prec = 1
    while True:
        prec = prec + 8 * i
        if number <= prec:
            return i
        i += 1

def get_ring_centers(ring_number):
    centers = []
    for j in range(0, 4):
        value = (ring_number * 3 + ring_number - 3) * ring_number + 1
        value += j * ring_number * 2
        centers.append(value)
    return centers

class UnitTest(unittest.TestCase):
    def test_rn(self):
        self.assertEqual(get_ring_number(1), 0)
        self.assertEqual(get_ring_number(7), 1)
        self.assertEqual(get_ring_number(14), 2)
        self.assertEqual(get_ring_number(46), 3)

    def test_rc(self):
        self.assertEqual(get_ring_centers(0), [1, 1, 1, 1])
        self.assertEqual(get_ring_centers(1), [2, 4, 6, 8])
        self.assertEqual(get_ring_centers(2), [11, 15, 19, 23])
        self.assertEqual(get_ring_centers(3), [28, 34, 40, 46])
        self.assertEqual(get_ring_centers(4), [53, 61, 69, 77])

    def test_solve(self):
        self.assertEqual(solve("1\n"), 0)
        self.assertEqual(solve("12\n"), 3)
        self.assertEqual(solve("23\n"), 2)
        self.assertEqual(solve("1024\n"), 31)

    def test_lambda(self):
        get_closest = get_closest_distance(0)
        self.assertEqual(get_closest(0), 0)
        self.assertEqual(get_closest(2), 2)
        get_closest = get_closest_distance(12)
        self.assertEqual(get_closest(10), 2)
        self.assertEqual(get_closest(15), 3)
