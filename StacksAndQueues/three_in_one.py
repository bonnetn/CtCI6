import unittest


class MultipleStack():
    def __init__(self, n):
        self.N = n
        self.arr = [0, 1, 2]

    def push(self, n, value):
        if n >= self.N:
            return None
        head_pos = self.arr[n]
        new_pos = head_pos + self.N
        if new_pos >= len(self.arr):
            self.arr = self.arr + [0] * self.N
        self.arr[new_pos] = value
        self.arr[n] = new_pos

    def pop(self, n):
        if n >= self.N:
            return None
        head_pos = self.arr[n]
        if head_pos < 3:
            return None

        self.arr[n] = self.arr[n] - self.N
        return self.arr[head_pos]

    def peek(self, n):
        if n >= self.N:
            return None
        head_pos = self.arr[n]
        if head_pos < 3:
            return None

        return self.arr[head_pos]


class ThreeInOneStack(MultipleStack):
    def __init__(self):
        super().__init__(3)


class Test(unittest.TestCase):

    def test_stack(self):
        s = ThreeInOneStack()

        for i in range(10):
            s.push(0, i)
        for i in range(5):
            s.push(1, 2 * i)
        for i in range(30):
            s.push(2, i * 10)

        for i in reversed(range(30)):
            assert s.pop(2) == i*10
        assert s.pop(2) is None

        assert s.peek(1) == 2*4
        assert s.peek(1) == 2*4


if __name__ == "__main__":
    unittest.main()
