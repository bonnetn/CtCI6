import unittest


class CyclicDep(Exception):
    pass


def dfs(dep, node, visited, build_order_set):
    if node in visited:
        raise CyclicDep()

    if node in build_order_set:  # already evaluated by a previous DFS, assume it's satisfied
        return []

    visited.add(node)
    path = []
    for n in dep[node]:
        path += dfs(dep, n, visited, build_order_set)

    return path + [node]


def build_order(dep):
    build_order_seq = []
    build_order_set = set()
    try:
        for node in dep:
            temp = dfs(dep, node, set(), build_order_set)
            build_order_seq += temp
            build_order_set.update(temp)
    except CyclicDep:
        return False

    return build_order_seq


class Test(unittest.TestCase):

    def test_build_order(self):
        dependencies = {
            0: set(),
            1: {0},
            2: {0},
            3: {1, 2},
            4: {0},
        }
        bo = build_order(dependencies)
        assert bo == [0, 1, 2, 3, 4]

    def test_build_order_cyclic(self):
        dependencies = {
            0: set(),
            1: {3},
            2: {0},
            3: {1, 2},
            4: {0},
        }
        assert build_order(dependencies) == False


if __name__ == "__main__":
    unittest.main()
