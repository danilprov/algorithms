from AdjacencyMatrixGraph import AdjacencyMatrixGraph


class Queue:
    def __init__(self):
        self.queue = []

    def dequeue(self):
        elem = self.queue[0]
        self.queue = self.queue[1:]

        return elem

    def add(self, elem):
        self.queue.append(elem)

    def is_empty(self):
        return not self.queue


class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0

    def pop(self):
        if self.len > 0:
            elem = self.stack[-1]
            self.stack = self.stack[:-1]
        else:
            raise ValueError("Stack is empty")

        return elem

    def push(self, elem):
        self.stack.append(elem)
        self.len += 1


def get_sources(vertices_powers):
    sources = []
    for i in range(len(vertices_powers)):
        if vertices_powers[i] == 0:
            sources.append(i)

    return sources


def demoucron_sorting(graph: AdjacencyMatrixGraph):
    """
    takes as an input a directed graph represented by Adjacent vectors:
    Example for undirected graph
    Graph                 Adjacent vectors
    0 - 1                  1 - -
      / |      4      ->   0 2 3
    2 - 3                  1 3 -
                           1 2 -
                           4 - -

    returns topological sorting of nodes

    1. from Adjacent vectors to Adjacent matrix
    2. calculating degree for each node
    3. adding to queue nodes with power 0
    4. dequeueing a node and adjusting power of each node

    questions:
    what do I do if there is no sources in the graph?
    i.e., if every vertex has incoming edges.
    """
    num_vertices = graph.get_num_vertices()
    adjacency_matrix = graph.get_adjacency_matrix()
    result = [[] for _ in range(num_vertices)]
    queue = Queue()
    level = 0

    # calculate power of each node from adjacency_matrix
    vertices_powers = [0 for _ in range(num_vertices)]
    for i, v in enumerate(graph.get_vertices()):
        vertices_powers[i] = graph.get_incoming_vertex_power(v)

    # main loop
    sources_idxs = get_sources(vertices_powers)
    while len(sources_idxs) != 0:
        for idx in sources_idxs:
            queue.add((idx, level))
            vertices_powers[idx] = -1

        while not queue.is_empty():
            # remove nodes and adjust nodes degrees
            v_idx, _level = queue.dequeue()
            row = adjacency_matrix[v_idx]
            for i in range(num_vertices):
                vertices_powers[i] -= row[i][0]
            result[_level].append(graph.get_key_by_value(v_idx))

        sources_idxs = get_sources(vertices_powers)
        level += 1

    return result


def dfs_util(v, visited, graph, depth=0):
    if visited[v]:
        return
    visited[v] = depth
    for neig in graph.get_adjacent_vertices(v):
        if not visited[neig]:
            dfs_util(neig, visited, graph, depth+1)


def tarjan_sorting(graph):
    num_vertices = graph.get_num_vertices()
    result = []

    # calculate power of each node from graph
    sources = []
    for i, v in enumerate(graph.get_vertices()):
        v_power = graph.get_incoming_vertex_power(v)
        if v_power == 0:
            sources.append(v)

    # main loop
    visited = dict.fromkeys(graph.get_vertices(), 0)
    for v in sources:
        dfs_util(v, visited, graph)

    max_depth = max(visited.values())
    for depth in range(max_depth + 1):
        result.append([k for k, v in visited.items() if v == depth])

    return result


if __name__ == '__main__':
    from AdjacencySetGraph import AdjacencySetGraph

    """
    0 1 0 0 0 
    0 0 1 1 0
    0 0 0 1 0
    0 0 0 0 0
    0 0 0 0 1
    ---------
    0 1 1 2 1 -> 0
    0 1 0 0 0
    ---------
    - 0 1 2 1 -> 1
    0 0 1 1 0
    ---------
    - - 0 1 1 -> 2
    0 0 0 1 0
    ---------
    - - - 0 1 -> 3
    """

    with open('resources/graph.4.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]

    print(lines)
    graph = AdjacencyMatrixGraph(None, True, lines)
    print(graph.adjacency_matrix)

    result = demoucron_sorting(graph)
    print(result)

    with open('resources/graph.4.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]
    graph = AdjacencySetGraph(None, True, lines)
    print(graph.adjacency_set)

    res = tarjan_sorting(graph)
    print(res)
