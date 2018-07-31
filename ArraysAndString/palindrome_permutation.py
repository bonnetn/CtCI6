import unittest
from collections import Counter


def palindrome_permutation(s):
    s = s.replace(" ", "").lower()
    c = Counter(s)
    single_letters = filter(lambda x: c[x] == 1, c)
    return sum(1 for i in single_letters) <= 1


class Test(unittest.TestCase):
    def test_true(self):
        self.assertTrue(palindrome_permutation("Tact Coa"))


if __name__ == "__main__":
    unittest.main()
