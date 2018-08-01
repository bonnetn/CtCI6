import unittest


class Node():
    def __init__(self, next, value):
        self.next = next
        self.value = value


def return_kth_to_last(list, k):
    current = list
    running = list
    for i in range(k):
        if running is None:
            return None
        running = running.next

    while running is not None:
        running = running.next
        current = current.next

    return current


class Test(unittest.TestCase):

    def test_kth(self):
        n = Node(None, 5)
        n = Node(n, 4)
        n = Node(n, 3)
        n = Node(n, 2)
        n = Node(n, 1)

        assert return_kth_to_last(n, 3).value == 3


if __name__ == "__main__":
    unittest.main()
