import unittest


class BTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(t):
    if not t:
        return True, 0

    is_balanced_right, height_right = dfs(t.right)
    if not is_balanced_right:
        return False, None

    is_balanced_left, height_left = dfs(t.left)
    if not is_balanced_left:
        return False, None

    return abs(height_left - height_right) <= 1, 1 + max(height_left, height_right)


def check_balanced(t):
    balanced, height = dfs(t)
    return balanced


class Test(unittest.TestCase):

    def test_not_balanced(self):
        root = BTree(0)
        left = BTree(1)
        right = BTree(2)
        left_left = BTree(3)
        left_left_left = BTree(4)

        root.left = left
        root.right = right
        left.left = left_left
        left.left.left = left_left_left

        assert not check_balanced(root)

    def test_balanced(self):
        root = BTree(0)
        left = BTree(1)
        right = BTree(2)

        root.left = left
        root.right = right

        assert check_balanced(root)


if __name__ == "__main__":
    unittest.main()
