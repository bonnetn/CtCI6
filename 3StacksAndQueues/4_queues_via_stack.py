import unittest


class QueueViaStacks:
    def __init__(self):
        self.stack_write = []
        self.stack_read = []

    def enqueue(self, value):
        self.stack_write.append(value)

    def dequeue(self):
        self._fill_read_stack()
        return self.stack_read.pop()

    def front(self):
        self._fill_read_stack()
        return self.stack_read[-1]

    def _fill_read_stack(self):
        # If needed, will fill the read stack
        if not self.stack_read:
            while self.stack_write:
                self.stack_read.append(self.stack_write.pop())


class Test(unittest.TestCase):

    def test_queue(self):
        s = QueueViaStacks()

        for i in (1, 2, 3):
            s.enqueue(i)

        assert s.front() == 1

        for i in (1, 2, 3):
            assert s.dequeue() == i


if __name__ == "__main__":
    unittest.main()
