import unittest


def dfs(graph, explored, current, goal):
    if current == goal:
        return True

    for neighbour in graph[current]:
        if neighbour not in explored:
            explored.add(neighbour)
            if dfs(graph, explored, neighbour, goal):
                return True

    return False


def route_between_nodes(graph, node1, node2):
    return dfs(graph, set(), node1, node2)


class Test(unittest.TestCase):

    def test_no_route_disjoint(self):
        # 0 --> 1
        # |
        # v
        # 2
        #
        # 3 --> 4

        graph = {
            0: {1, 2},
            1: {},
            2: {},
            3: {4},
            4: {},
        }
        assert not route_between_nodes(graph, 0, 4)

    def test_no_route(self):
        # 0 --> 1
        # |
        # v
        # 2
        # ^
        # |
        # 3 --> 4

        graph = {
            0: {1, 2},
            1: {},
            2: {},
            3: {4, 2},
            4: {},
        }
        assert not route_between_nodes(graph, 0, 4)

    def test_route(self):
        # 0 --> 1
        # |
        # v
        # 2
        # |
        # v
        # 3 --> 4

        graph = {
            0: {1, 2},
            1: {},
            2: {3},
            3: {4},
            4: {},
        }
        assert route_between_nodes(graph, 0, 4)


if __name__ == "__main__":
    unittest.main()
