from abc import ABC, abstractmethod


class IGraph:
    @abstractmethod
    def add_vertex(self, vertex_from, vertex_to, weight):
        pass

    @abstractmethod
    def add_edge(self, e):
        pass

    @abstractmethod
    def is_adjacent(self, v1, v2):
        pass

    @abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abstractmethod
    def get_vertex_power(self, v):
        pass

    @abstractmethod
    def get_weight_between_vertices(self, vertex_from, vertex_to):
        pass

    @abstractmethod
    def create_graph_from_list_of_edges(self, list_of_edges):
        pass

    @abstractmethod
    def get_vertices(self):
        pass

    @abstractmethod
    def get_num_vertices(self):
        pass
