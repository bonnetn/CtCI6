import unittest


def one_away(a, b):
    if len(a) < len(b):
        a, b = b, a

    for i, bLetter in enumerate(b):
        if bLetter != a[i]:
            return b[i:] == a[i + 1:] or a[i + 1:] == b[i + 1:]

    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(one_away("pale", "bale"))
        self.assertTrue(one_away("pale", "pales"))
        self.assertTrue(one_away("pale", "ple"))
        self.assertFalse(one_away("pale", "bake"))


if __name__ == "__main__":
    unittest.main()
