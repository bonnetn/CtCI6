import unittest


class Node():
    def __init__(self, next, value):
        self.next = next
        self.value = value


def remove_dups(list):
    current = list
    running = list
    items = {current.value}

    while running.next is not None:
        if running.value not in items:
            items.add(running.value)
            current.next = running
            current = running
        running = running.next

    return list


class Test(unittest.TestCase):

    def test_dups(self):
        n = Node(None, 1)
        n = Node(n, 5)
        n = Node(n, 2)
        n = Node(n, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 2)
        n = Node(n, 1)

        n = remove_dups(n)

        for i in range(1, 6):
            assert n.value == i
            n = n.next

        assert n.next is None


if __name__ == "__main__":
    unittest.main()
