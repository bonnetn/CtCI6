import unittest


class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


def loop_detection(linked_list):
    nodes = set()
    cursor = linked_list
    while cursor is not None:
        if cursor in nodes:
            return cursor
        nodes.add(cursor)
        cursor = cursor.next

    return False


class Test(unittest.TestCase):

    def test_loop_detection(self):
        tail = n = Node(None, 5)
        n = Node(n, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)
        tail.next = n

        assert loop_detection(n) == n

    def test_not_loop_detection(self):
        n = Node(None, 5)
        n = Node(n, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)
        assert not loop_detection(n)


if __name__ == "__main__":
    unittest.main()
