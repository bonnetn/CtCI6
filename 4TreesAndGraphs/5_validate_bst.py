import unittest


class BTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_bst(tree):
    is_bst, _ = dfs(tree)
    return is_bst


def dfs(tree):
    if tree is None:
        return True, None

    is_bst_left, max_left = dfs(tree.left)
    if not is_bst_left:
        return False, None

    is_bst_right, max_right = dfs(tree.right)
    if not is_bst_right:
        return False, None

    if tree.left and tree.right:
        return max_left <= tree.value < max_right, max_right

    if tree.left:
        return max_left <= tree.value, tree.value

    if tree.right:
        return tree.value < max_right, max_right

    return True, tree.value


class Test(unittest.TestCase):

    def test_not_bst(self):
        root = BTree(1)
        left = BTree(0)
        right = BTree(2)
        left_left = BTree(10)

        root.left = left
        root.right = right
        left.left = left_left

        assert not validate_bst(root)

    def test_bst(self):
        root = BTree(1)
        left = BTree(0)
        right = BTree(2)

        root.left = left
        root.right = right

        assert validate_bst(root)


if __name__ == "__main__":
    unittest.main()
