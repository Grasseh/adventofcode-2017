# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    lines = fn_input[:-1].split("\n")
    return len(list(filter(is_valid_passphrase, lines)))

def is_valid_passphrase(phrase):
    words = phrase.split(" ")
    return len(words) == len(set(words))

class UnitTest(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_passphrase("aa bb cc dd ee"))
        self.assertTrue(is_valid_passphrase("aa bb cc dd aaa"))
        self.assertFalse(is_valid_passphrase("aa bb cc dd aa"))

    def test_solve(self):
        self.assertEqual(solve("aa bb cc dd ee\naa bb cc dd aaa\naa bb cc dd aa\n"), 2)
