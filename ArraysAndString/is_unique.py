import string
import unittest
from collections import Counter

ALL_LETTERS = Counter(string.printable)


def is_unique(s):
    return Counter(s) | ALL_LETTERS == ALL_LETTERS


class Test(unittest.TestCase):
    def test_non_unique(self):
        self.assertFalse(is_unique("the quick brown fox jumps over the lazy dog"))

    def test_unique(self):
        self.assertTrue(is_unique("abcdefg"))


if __name__ == "__main__":
    unittest.main()
