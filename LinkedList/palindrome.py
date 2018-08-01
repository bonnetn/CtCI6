import unittest


class Node():
    def __init__(self, next, value):
        self.next = next
        self.value = value


def palindrome(linked_list):
    stack = []

    cursor = linked_list
    while cursor is not None:
        stack.append(cursor.value)
        cursor = cursor.next

    cursor = linked_list
    while cursor is not None:
        if cursor.value != stack.pop():
            return False
        cursor = cursor.next

    return True


class Test(unittest.TestCase):

    def test_palindrome(self):
        n = Node(None, 1)
        n = Node(n, 2)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)
        assert palindrome(n)

    def test_not_palindrome(self):
        n = Node(None, 5)
        n = Node(n, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)
        assert not palindrome(n)


if __name__ == "__main__":
    unittest.main()
