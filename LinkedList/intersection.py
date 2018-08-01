import unittest


class Node():
    def __init__(self, next, value):
        self.next = next
        self.value = value


def intersection(a, b):
    nodes = set()
    while a is not None:
        nodes.add(a)
        a = a.next

    while b is not None:
        if b in nodes:
            return True
        b = b.next

    return False


class Test(unittest.TestCase):

    def test_intersection(self):
        n = Node(None, 5)
        n = Node(n, 4)
        n = Node(n, 3)
        n1 = Node(n, 2)
        n1 = Node(n1, 1)
        n2 = Node(n, 20)
        n2 = Node(n2, 10)
        assert intersection(n1, n2)

    def test_not_intersection(self):
        n = Node(None, 5)
        n = Node(n, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)

        n2 = Node(None, 5)
        n2 = Node(n2, 4)
        n2 = Node(n2, 3)
        n2 = Node(n2, 2)
        n2 = Node(n2, 1)
        assert not intersection(n, n2)


if __name__ == "__main__":
    unittest.main()
