import itertools
import unittest


def string_compression(s):
    compressed = []
    for k, v in itertools.groupby(s):
        compressed += [k, str(sum(1 for i in v))]

    compressed = "".join(compressed)
    if len(s) < len(compressed):
        return s
    return compressed


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_compression("AAABBCCCA"), "A3B2C3A1")
        self.assertEqual(string_compression("ABC"), "ABC")
        self.assertEqual(string_compression("A" * 1337), "A1337")


if __name__ == "__main__":
    unittest.main()
