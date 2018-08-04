import unittest


class Node:
    def __init__(self, next, value):
        self.next = next
        self.value = value


def partition(linked_list, x):
    current = linked_list
    greater_head = None
    lesser_tail = None
    lesser_head = None
    while current is not None:
        next_node = current.next
        if current.value > x:
            current.next = greater_head
            greater_head = current
        else:
            if lesser_tail:
                lesser_tail.next = current
            else:
                lesser_head = current
            current.next = None
            lesser_tail = current
        current = next_node

    if lesser_head is None:
        return greater_head

    lesser_tail.next = greater_head

    return lesser_head


class Test(unittest.TestCase):

    def test_partition(self):
        n = Node(None, 1)
        n = Node(n, 1)
        n = Node(n, 11)
        n = Node(n, 11)
        n = Node(n, 11)

        n = partition(n, 5)

        for i in (1, 1, 11, 11, 11):
            assert n.value == i
            n = n.next


if __name__ == "__main__":
    unittest.main()
