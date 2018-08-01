import unittest


# O(N)
def find_string(pat, txt):
    # Basic implementation of KMP search
    # Could have used python's str.find which is probably more efficient, but it was more fun implementing that.

    if len(pat) > len(txt):
        return False

    # Compute the prefix table
    prefix_tbl = [0] * len(pat)
    for i in range(1, len(pat)):
        j = prefix_tbl[i - 1]
        while j > 0 and pat[i] != pat[j]:
            j = prefix_tbl[j - 1]
        if pat[i] == pat[j]:
            j += 1
        prefix_tbl[i] = j

    # Do the actual search
    j = 0
    for i, letter in enumerate(txt):
        if letter == pat[j]:
            j += 1
            if j == len(prefix_tbl):
                return i - len(pat) + 1
        else:
            j = prefix_tbl[j - 1]

    return -1


# O(N)
def string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    if find_string(str1, str2 + str2) != -1:
        return True
    else:
        return False


class Test(unittest.TestCase):
    def test_find(self):
        pat = "abc"
        txt = "test abc test"

        assert find_string(pat, txt) == 5

    def test_rotation(self):
        rot = "abc"
        txt = "bca"

        assert string_rotation(rot, txt)
        assert not string_rotation(rot, "lol")


if __name__ == "__main__":
    unittest.main()
