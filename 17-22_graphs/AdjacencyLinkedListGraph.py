from abc import ABC
from IGraph import IGraph


class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class _Node:
    def __init__(self, vertex=None, weight=None):
        self.vertex = vertex
        self.weight = weight
        self.next = None


class AdjacencyLinkedListGraph(IGraph, ABC):
    """
    Graph representation as a linked list:
    [
     [2,-]->
     [1,-]-> [3,-]->[4,-]->
     [2,-]-> [4,-]->
     [2,-]-> [3,-]->
     [5,-]-> [5,-]->
    ]

    Advantages:
    1. Consumes space of E
    2. Getting adjacent vertices is simple O(S_a) (where S_a is a power of vertex a)
    3. Check if 2 vertices adjacent is relatively simple - O(S_a)
    4. Adding and removing an edge is simple
    """
    def __init__(self, size, directed, list_of_edges=None):
        self.directed = directed
        if not list_of_edges:
            self.adjacency_list = dict()
            self.num_vertices = 0
            self.num_edges = 0
            self.edges = []
        else:
            self.create_graph_from_list_of_edges(list_of_edges)

    def create_graph_from_list_of_edges(self, list_of_edges):
        self.num_vertices = int(list_of_edges[0][0])
        #self.num_edges = int(list_of_edges[0][1])
        self.num_edges = 0 # we will count them in `add_edge`
        self.adjacency_list = dict()
        self.edges = []
        for i in range(1, len(list_of_edges)):
            self.add_edge(list_of_edges[i])

    def add_empty_vertex(self, v):
        if v not in self.adjacency_list:
            self.adjacency_list[v] = None

    def add_vertex(self, vertex_from, vertex_to, weight):
        """add vertex_to to linked list of vertex_from"""
        if vertex_from not in self.adjacency_list or self.adjacency_list[vertex_from] is None:
            self.adjacency_list[vertex_from] = _Node(vertex_to, weight)
        else:
            target_list = self.adjacency_list[vertex_from]
            while target_list.next:
                target_list = target_list.next
            target_list.next = _Node(vertex_to, weight)

    def add_edge(self, e):
        vertex_from = str(e[0])
        vertex_to = str(e[1])
        try:
            weight = int(e[2])
        except:
            weight = None
        self.num_edges += 1
        self.edges.append(Edge(vertex_from, vertex_to, weight))
        self.add_vertex(vertex_from, vertex_to, weight)

        # if undirected graph: add vertex_from to linked list of vertex_to
        if not self.directed:
            self.add_vertex(vertex_to, vertex_from, weight)

    def is_adjacent(self, vertex_from, vertex_to):
        if vertex_from not in self.adjacency_list or vertex_to not in self.adjacency_list:
            raise ValueError("Illegal argument exception")

        target_list = self.adjacency_list[vertex_from]
        while target_list:
            if target_list.key == vertex_to:
                return True
            target_list = target_list.next

        return False

    def get_adjacent_vertices(self, v):
        assert v in self.adjacency_list, "Vertex doesn't exist"

        adjacent_vertices = []
        target_list = self.adjacency_list[v]
        while target_list:
            adjacent_vertices.append(target_list.vertex)
            target_list = target_list.next

        return adjacent_vertices

    def get_weight_between_vertices(self, vertex_from, vertex_to):
        if vertex_from not in self.adjacency_list or vertex_to not in self.adjacency_list:
            raise ValueError("Illegal argument exception")

        target_list = self.adjacency_list[vertex_from]
        while target_list:
            if target_list.vertex == vertex_to:
                return target_list.weight
            target_list = target_list.next

        return None

    def get_vertex_power(self, v):
        assert v in self.adjacency_list, "Vertex doesn't exist"

        power = 0
        target_list = self.adjacency_list[v]
        while target_list:
            power += 1
            target_list = target_list.next

        return power

    def get_vertices(self):
        return self.adjacency_list.keys()

    def get_num_vertices(self):
        return self.num_vertices

    def get_edges(self):
        return self.edges


if __name__ == "__main__":
    with open('resources/graph.6.in') as f:
        lines = [line.rstrip('\n').split(' ') for line in f]

    print(lines)
    graph = AdjacencyLinkedListGraph(None, False, lines)
    print(graph.adjacency_list)
    print(graph.num_vertices)
    print(graph.num_edges)
    print(graph.get_vertex_power('a'))
    print(graph.get_adjacent_vertices('a'))
    print(graph.get_weight_between_vertices('a', 'b'))
