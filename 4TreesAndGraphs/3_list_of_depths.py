import unittest


class BTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(tree, list_depth, current_depth):
    if tree is None:
        return

    if current_depth not in list_depth:
        list_depth[current_depth] = []
    list_depth[current_depth] += [tree]

    dfs(tree.left, list_depth, current_depth + 1)
    dfs(tree.right, list_depth, current_depth + 1)


def list_of_depth(tree):
    result = {}
    dfs(tree, result, 0)
    return result


class Test(unittest.TestCase):

    def test_depth(self):
        root = BTree(0)
        left = BTree(1)
        right = BTree(2)
        left_left = BTree(3)

        root.left = left
        root.right = right
        left.left = left_left

        assert list_of_depth(root) == {
            0: [root],
            1: [left, right],
            2: [left_left]
        }


if __name__ == "__main__":
    unittest.main()
