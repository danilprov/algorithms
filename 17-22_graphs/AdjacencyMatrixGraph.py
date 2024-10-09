from abc import ABC
from IGraph import IGraph


class AdjacencyMatrixGraph(IGraph, ABC):
    """
    Graph representation as a 2d matrix:
    [
     [0, 1, 0, 0, 0],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 1, 1, 0, 0],
     [0, 0, 0, 0, 2]
    ]
    1  3  2  2  2

    Advantages:
    1. Getting adjacent vertices is relatively simple O(V)
    2. Check if 2 vertices adjacent is simple - O(1)

    Disadvantages of this approach:
    1. Consumes space of V^2

    Questions:
    1. How to deal with weighted graph in this case? Perhaps we can store two values in each cell

    I assume that 0 value mean that there is no edge between two vertices, whereas
    positive value means that there is an edge and it specifies its weight
    """
    def __init__(self, size, directed, list_of_edges=None):
        self.directed = directed
        self.v_idx_mapping = {}
        self.last_idx = 0
        if not list_of_edges:
            self.adjacency_matrix = [[(0, float('inf'))] * size for _ in range(size)]
            self.num_vertices = 0
            self.num_edges = 0
        else:
            self.create_graph_from_list_of_edges(list_of_edges)

    def create_graph_from_list_of_edges(self, list_of_edges):
        self.num_vertices = int(list_of_edges[0][0])
        #self.num_edges = int(list_of_edges[0][1])
        self.num_edges = 0 # we will count them in `add_edge`
        self.adjacency_matrix = [[(0, float('inf'))] * self.num_vertices for _ in range(self.num_vertices)]
        for i in range(1, len(list_of_edges)):
            self.add_edge(list_of_edges[i])

    def add_vertex(self, vertex_from, vertex_to, weight):
        if vertex_from not in self.v_idx_mapping:
            self.v_idx_mapping[vertex_from] = self.last_idx
            self.last_idx += 1
        if vertex_to not in self.v_idx_mapping:
            self.v_idx_mapping[vertex_to] = self.last_idx
            self.last_idx += 1

        vertex_from_idx = self.v_idx_mapping[vertex_from]
        vertex_to_idx = self.v_idx_mapping[vertex_to]
        self.adjacency_matrix[vertex_from_idx][vertex_to_idx] = (1, weight)

    def add_edge(self, e):
        vertex_from = str(e[0])
        vertex_to = str(e[1])
        try:
            weight = int(e[2])
        except:
            weight = None

        self.num_edges += 1
        self.add_vertex(vertex_from, vertex_to, weight)
        if not self.directed:
            self.add_vertex(vertex_to, vertex_from, weight)

    def is_adjacent(self, vertex_from, vertex_to):
        if vertex_from not in self.v_idx_mapping or vertex_to not in self.v_idx_mapping:
            raise ValueError("Illegal argument exception")

        vertex_from_idx = self.v_idx_mapping[vertex_from]
        vertex_to_idx = self.v_idx_mapping[vertex_to]
        return self.adjacency_matrix[vertex_from_idx][vertex_to_idx] > 0

    def get_adjacent_vertices(self, v):
        assert v in self.v_idx_mapping, "Vertex doesn't exist"
        adjacent_vertices = []
        v_idx = self.v_idx_mapping[v]
        for i in range(self.num_vertices):
            if self.adjacency_matrix[v_idx][i][0] == 1:
                adjacent_vertex = self.get_key_by_value(i)
                adjacent_vertices.append(adjacent_vertex)

        return tuple(adjacent_vertices)

    def get_key_by_value(self, value):
        return list(self.v_idx_mapping.keys())[list(self.v_idx_mapping.values()).index(value)]

    def get_value_by_key(self, vertex):
        return self.v_idx_mapping[vertex]

    def get_weight_between_vertices(self, vertex_from, vertex_to):
        if vertex_from not in self.v_idx_mapping or vertex_to not in self.v_idx_mapping:
            raise ValueError("Illegal argument exception")

        vertex_from_idx = self.v_idx_mapping[vertex_from]
        vertex_to_idx = self.v_idx_mapping[vertex_to]
        return self.adjacency_matrix[vertex_from_idx][vertex_to_idx][1]

    def get_vertex_power(self, v):
        assert v in self.v_idx_mapping, "Vertex doesn't exist"
        vertex_power = 0
        v_idx = self.v_idx_mapping[v]
        for i in range(self.num_vertices):
            vertex_power += self.adjacency_matrix[v_idx][i][0]

        return vertex_power

    def get_incoming_vertex_power(self, v):
        assert v in self.v_idx_mapping, "Vertex doesn't exist"
        vertex_power = 0
        v_idx = self.v_idx_mapping[v]
        for i in range(self.num_vertices):
            vertex_power += self.adjacency_matrix[i][v_idx][0]

        return vertex_power

    def get_vertices(self):
        return self.v_idx_mapping.keys()

    def get_adjacency_matrix(self):
        adjacency_matrix = []
        for i in range(self.num_vertices):
            temp = [0] * self.num_vertices
            for j in range(self.num_vertices):
                temp[j] = self.adjacency_matrix[i][j]
            adjacency_matrix.append(temp)
        return adjacency_matrix

    def get_weight_matrix(self):
        weight_matrix = []
        for i in range(self.num_vertices):
            temp = [0] * self.num_vertices
            for j in range(self.num_vertices):
                temp[j] = self.adjacency_matrix[i][j][1]
            weight_matrix.append(temp)
        return weight_matrix

    def get_num_vertices(self):
        return self.num_vertices


if __name__ == "__main__":
    with open('resources/graph.2.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]

    print(lines)
    graph = AdjacencyMatrixGraph(None, False, lines)
    print(graph.adjacency_matrix)
    print(graph.num_vertices)
    print(graph.num_edges)
    print(graph.get_vertex_power('2'))
    print(graph.get_adjacent_vertices('2'))
