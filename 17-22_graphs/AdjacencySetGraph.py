from abc import ABC
from IGraph import IGraph


class AdjacencySetGraph(IGraph, ABC):
    """
    Graph representation as a list of lists/arrays:
    [
     [2],
     [1, 3, 4],
     [2, 4],
     [2, 3],
     [5, 5]
    ]

    Advantages:
    1. Consumes space of E
    2. Getting adjacent vertices is simple O(S_a) (where S_a is a power of vertex a)
    3. Check if 2 vertices adjacent is relatively simple - O(S_a)

    Disadvantages of this approach:
    1. Indices don't mean anything in each of the arrays
    2. In a classical array (from C) we also need to resize arrays dynamically
    3. Removing an edge will require shifting the corresponding array

    Questions:
    1. How to deal with weighted graph in this case?
    2. How to deal with parallel edges if they are allowed?
    """
    def __init__(self, size, directed, list_of_edges=None):
        self.directed = directed
        if not list_of_edges:
            self.adjacency_set = {}
            self.num_vertices = 0
            self.num_edges = 0
        else:
            self.create_graph_from_list_of_edges(list_of_edges)

    def create_graph_from_list_of_edges(self, list_of_edges):
        self.num_vertices = int(list_of_edges[0][0])
        #self.num_edges = int(list_of_edges[0][1])
        self.num_edges = 0 # we will count them in `add_edge`
        self.adjacency_set = {}
        for i in range(1, len(list_of_edges)):
            self.add_edge(list_of_edges[i])

    def add_vertex(self, vertex_from, vertex_to, weight):
        if vertex_from not in self.adjacency_set:
            self.adjacency_set[vertex_from] = [vertex_to]
        else:
            self.adjacency_set[vertex_from].append(vertex_to)

        if vertex_to not in self.adjacency_set:
            self.adjacency_set[vertex_to] = []

    def add_edge(self, e):
        vertex_from = str(e[0])
        vertex_to = str(e[1])
        weight = None
        self.num_edges += 1
        self.add_vertex(vertex_from, vertex_to, weight)
        if not self.directed:
            self.add_vertex(vertex_to, vertex_from, weight)

    def is_adjacent(self, vertex_from, vertex_to):
        if vertex_from not in self.adjacency_set or vertex_to not in self.adjacency_set:
            raise ValueError("Illegal argument exception")

        return vertex_to in self.adjacency_set[vertex_from]

    def get_adjacent_vertices(self, v):
        assert v in self.adjacency_set, "Vertex doesn't exist"
        return tuple(self.adjacency_set[v])

    def get_weight_between_vertices(self, vertex_from, vertex_to):
        raise NotImplementedError

    def get_vertex_power(self, v):
        assert v in self.adjacency_set, "Vertex doesn't exist"
        return len(self.adjacency_set[v])

    def get_vertices(self):
        return self.adjacency_set.keys()

    def get_incoming_vertex_power(self, v):
        assert v in self.adjacency_set, "Vertex doesn't exist"
        vertex_power = 0
        for vv in self.get_vertices():
            vertex_power += v in self.adjacency_set[vv]

        return vertex_power

    def get_num_vertices(self):
        return self.num_vertices


if __name__ == "__main__":
    with open('resources/graph.2.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]

    print(lines)
    graph = AdjacencySetGraph(None, False, lines)
    print(graph.adjacency_set)
    print(graph.num_vertices)
    print(graph.num_edges)
    print(graph.get_vertex_power('2'))
    print(graph.get_adjacent_vertices('2'))
    #print(graph.get_weight_between_vertices('1', '2'))