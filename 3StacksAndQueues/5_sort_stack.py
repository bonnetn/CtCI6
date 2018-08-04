import random
import unittest


def sort_stack(stack):
    result = []
    while stack:
        x = stack.pop()
        while result and result[-1] < x:
            stack.append(result.pop())
        result.append(x)

    return result


class Test(unittest.TestCase):

    def test_sort_stack(self):
        s = list(range(100))
        random.shuffle(s)

        s = sort_stack(s)

        for i in range(100):
            assert s.pop() == i


if __name__ == "__main__":
    unittest.main()
