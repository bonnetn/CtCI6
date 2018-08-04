import unittest
from collections import Counter


def check_permutation(a, b):
    return Counter(a) == Counter(b)


class Test(unittest.TestCase):
    def test_not_perm(self):
        self.assertFalse(check_permutation("abc", "bacz"))

    def test_perm(self):
        self.assertTrue(check_permutation("abc", "bac"))


if __name__ == "__main__":
    unittest.main()
