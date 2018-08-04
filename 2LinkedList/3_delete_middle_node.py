import unittest


class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


def remove_middle(list):
    current = list
    running = list.next

    while running is not None:
        running = running.next
        if running:
            running = running.next
        if running:
            current = current.next

    current.next = current.next.next
    return list


class Test(unittest.TestCase):

    def test_remove_middle_even(self):
        n = Node(None, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)

        n = remove_middle(n)

        assert n.next.next.value == 4

    def test_remove_middle_odd(self):
        n = Node(None, 5)
        n = Node(n, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)

        n = remove_middle(n)

        assert n.next.next.value == 4


if __name__ == "__main__":
    unittest.main()
