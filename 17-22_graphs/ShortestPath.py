from AdjacencyMatrixGraph import AdjacencyMatrixGraph


def floyd_warshall_shortest_path(graph: AdjacencyMatrixGraph):
    """
    find distances from every vertex to every other vertex in a weighted graph.
    Complexity is O(V^3)

    :param graph:
    :return:
    """

    weight_matrix = graph.get_weight_matrix()
    vertices = graph.get_vertices()

    for v_temp in vertices:
        for v_from in vertices:
            for v_to in vertices:
                k, i, j = (graph.get_value_by_key(v) for v in [v_temp, v_from, v_to])
                weight_matrix[i][j] = min(weight_matrix[i][j],
                                          weight_matrix[i][k] + weight_matrix[k][j])

    return weight_matrix


def dijkstra_shortest_path(target_v, graph: AdjacencyMatrixGraph):
    """
    find shortest path from a given vertex to every other vertex in a weighted graph.
    Weights must be non-negative. Worst-case complexity is O(V^2)

    :param target_v: given vertex
    :param graph: AdjacencyMatrixGraph
    :return: dict with distances to other vertex
    """
    vertices = graph.get_vertices()
    shortest_path = {v: float('inf') for v in vertices}
    shortest_path[target_v] = 0
    visited = {v: 0 for v in vertices}

    while sum(visited.values()) < graph.get_num_vertices():
        non_visited_costs = {k: (shortest_path.get(k, 0) + visited.get(k, 0) * 1000) for k in vertices}
        current_v = min(non_visited_costs, key=non_visited_costs.get)
        visited[current_v] = 1
        neighbours = graph.get_adjacent_vertices(current_v)
        for neig in neighbours:
            weight = graph.get_weight_between_vertices(current_v, neig)
            if shortest_path[current_v] + weight < shortest_path[neig]:
                shortest_path[neig] = shortest_path[current_v] + weight

    return shortest_path


if __name__ == '__main__':
    with open('resources/graph.7.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]

    print(lines)
    graph = AdjacencyMatrixGraph(None, True, lines)

    shortest_path = floyd_warshall_shortest_path(graph)
    assert shortest_path == [[1, -2, 6, 2],
                             [3, 1, 8, 4],
                             [-5, -7, 1, -4],
                             [-1, -3, 5, 1]]

    with open('resources/graph.8.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]

    print(lines)
    graph = AdjacencyMatrixGraph(None, False, lines)

    shortest_path = dijkstra_shortest_path('a', graph)
    assert shortest_path == {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 9, 'f': 8, 'g': 14}