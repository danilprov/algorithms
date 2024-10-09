from AdjacencyLinkedListGraph import AdjacencyLinkedListGraph


class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


def prim_algorithm(graph: AdjacencyLinkedListGraph):
    vertices = graph.get_vertices()
    cheapest_costs = dict.fromkeys(vertices, float('inf'))
    cheapest_edges = dict.fromkeys(vertices, None)
    visited = dict.fromkeys(vertices, 0)

    while sum(visited.values()) < graph.get_num_vertices():
        non_visited_costs = {k: (cheapest_costs.get(k, 0) + visited.get(k, 0) * 1000) for k in vertices}
        v = min(non_visited_costs, key=non_visited_costs.get)
        visited[v] = 1

        neighbours = graph.get_adjacent_vertices(v)
        for neig in neighbours:
            weight = graph.get_weight_between_vertices(v, neig)
            if weight < cheapest_costs[neig] and visited[neig] == 0:
                cheapest_costs[neig] = weight
                cheapest_edges[neig] = Edge(v, neig, weight)

    forest = AdjacencyLinkedListGraph(None, False)
    for v, e in cheapest_edges.items():
        if e is not None:
            forest.add_edge((e.v1, e.v2, e.weight))

    return forest


def kruskal_algorithm(graph: AdjacencyLinkedListGraph):
    sorted_edges = sorted(graph.get_edges(), key=lambda x: x.weight)
    forest = AdjacencyLinkedListGraph(None, False)
    for v in graph.get_vertices():
        forest.add_empty_vertex(v)
    i = 0

    while len(forest.get_edges()) < graph.get_num_vertices() - 1:
        edge = sorted_edges[i]
        if forest.get_vertex_power(edge.v1) == 0 or forest.get_vertex_power(edge.v2) == 0:
            forest.add_edge((edge.v1, edge.v2, edge.weight))
        else:
            visited = dict.fromkeys(graph.get_vertices(), 0)
            dfs_util(edge.v1, visited, forest)
            if visited[edge.v2] == 0:
                forest.add_edge((edge.v1, edge.v2, edge.weight))
        i += 1

    return forest


def dfs_util(v, visited, graph):
    if visited[v] == 1:
        return
    visited[v] = 1
    neighbours = graph.get_adjacent_vertices(v)
    for neig in neighbours:
        dfs_util(neig, visited, graph)


def kruskal_algorithm2(graph: AdjacencyLinkedListGraph):
    vertices = graph.get_vertices()
    sorted_edges = sorted(graph.get_edges(), key=lambda x: x.weight)
    parent_dict = dict(zip(vertices, vertices))
    forest = AdjacencyLinkedListGraph(None, False)
    for v in graph.get_vertices():
        forest.add_empty_vertex(v)

    for edge in sorted_edges:
        if find(edge.v1, parent_dict) != find(edge.v2, parent_dict):
            forest.add_edge((edge.v1, edge.v2, edge.weight))
            merge(edge.v1, edge.v2, parent_dict)

    return forest


# union find technique
def find(a, parents: dict):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a], parents)

    return parents[a]


def merge(a, b, parents: dict):
    root_a = find(a, parents)
    root_b = find(b, parents)
    if root_b != root_a:
        parents[root_a] = root_b


if __name__ == '__main__':
    with open('resources/graph.6.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]

    print(lines)
    graph = AdjacencyLinkedListGraph(None, False, lines)

    result = prim_algorithm(graph)
    sum_weights = 0
    for edge in result.get_edges():
        sum_weights += edge.weight
    print(sum_weights)

    result = kruskal_algorithm(graph)
    sum_weights = 0
    for edge in result.get_edges():
        sum_weights += edge.weight
    print(sum_weights)

    result = kruskal_algorithm2(graph)
    sum_weights = 0
    for edge in result.get_edges():
        sum_weights += edge.weight
    print(sum_weights)