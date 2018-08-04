import unittest


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, value):
        if not self.min_values:
            self.min_values.append(value)
        else:
            self.min_values.append(min(self.min(), value))

        self.stack.append(value)

    def pop(self):
        self.min_values.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def min(self):
        return self.min_values[-1]


class Test(unittest.TestCase):

    def test_stack(self):
        s = MinStack()

        for i in (1, 2, 3):
            s.push(i)

        assert s.peek() == 3
        assert s.min() == 1

        for i in (3, 2, 1):
            assert s.pop() == i

        for i in (10, 20, 30):
            s.push(i)

        print(s.min())
        assert s.min() == 10


if __name__ == "__main__":
    unittest.main()
