import unittest


def zero_matrix(m):
    rows = [False] * len(m)
    columns = [False] * len(m[0])

    for x, row in enumerate(m):
        for y, value in enumerate(row):
            if value == 0:
                rows[x] = True
                columns[y] = True

    for x, row in enumerate(m):
        for y, value in enumerate(row):
            if rows[x] or columns[y]:
                m[x][y] = 0

    return m


class Test(unittest.TestCase):
    def test_matrix_no_change(self):
        m = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        w = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        assert zero_matrix(m) == w

    def test_matrix_edge(self):
        m = [[0, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]
        w = [[0, 0, 0],
             [0, 5, 0],
             [0, 0, 0]]
        assert zero_matrix(m) == w

    def test_matrix_center(self):
        m = [[1, 2, 3],
             [4, 0, 6],
             [7, 8, 9]]
        w = [[1, 0, 3],
             [0, 0, 0],
             [7, 0, 9]]
        assert zero_matrix(m) == w


if __name__ == "__main__":
    unittest.main()
