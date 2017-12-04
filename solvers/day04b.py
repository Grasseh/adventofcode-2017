# pylint: disable=missing-docstring
import unittest

def solve(fn_input):
    lines = fn_input[:-1].split("\n")
    return len(list(filter(is_valid_passphrase, lines)))

def is_valid_passphrase(phrase):
    words = phrase.split(" ")
    return len(words) == len(set(list(map(''.join,list(map(sorted, words))))))

class UnitTest(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid_passphrase("abcde fghij"))
        self.assertTrue(is_valid_passphrase("a ab abc abd abf abj"))
        self.assertTrue(is_valid_passphrase("iiii oiii ooii oooi oooo"))
        self.assertFalse(is_valid_passphrase("oiii ioii iioi iiio"))
        self.assertFalse(is_valid_passphrase("abcde xyz ecdab"))
