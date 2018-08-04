import math
import unittest
from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])


def rotate90(pos, center):
    # (v2.x + v2.y*1j) * exp(1j*angleInRad)
    pos = Position(pos.x - center, pos.y - center)
    x = -pos.y + center
    y = pos.x + center
    return Position(x, y)


def rotate_matrix(m):
    middle = len(m) // 2
    for x in range(math.ceil(len(m) / 2)):
        for y in range(len(m) // 2):
            p1 = Position(x, y)
            p2 = rotate90(p1, middle)
            p3 = rotate90(p2, middle)
            p4 = rotate90(p3, middle)

            temp = m[p1.x][p1.y]
            m[p1.x][p1.y] = m[p2.x][p2.y]
            m[p2.x][p2.y] = m[p3.x][p3.y]
            m[p3.x][p3.y] = m[p4.x][p4.y]
            m[p4.x][p4.y] = temp
    return m


class Test(unittest.TestCase):
    def test(self):
        m = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        wanted = [[7, 4, 1],
                  [8, 5, 2],
                  [9, 6, 3]]

        self.assertEqual(rotate_matrix(m), wanted)


if __name__ == "__main__":
    unittest.main()
