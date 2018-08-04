import unittest


class BSTree:
    def __init__(self, value):
        self.value = value


def minimal_tree(l):
    if not l:
        return

    middle = len(l) // 2
    tree = BSTree(l[middle])
    tree.left = minimal_tree(l[:middle])
    tree.right = minimal_tree(l[middle + 1:])

    return tree


def get_height(t):
    if not t:
        return 0
    return 1 + max(get_height(t.left), get_height(t.right))


class Test(unittest.TestCase):

    # 1023 is a maximum capacity for a binary search tree of height 10
    def test_tree(self):
        tree = minimal_tree(list(range(1023)))
        assert get_height(tree) == 10

    def test_tree_2(self):
        tree = minimal_tree(list(map(lambda x: 2**x, range(1023))))
        assert get_height(tree) == 10


if __name__ == "__main__":
    unittest.main()
