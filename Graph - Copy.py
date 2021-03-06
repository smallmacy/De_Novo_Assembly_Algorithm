class Graph:
    def __init__(self):
        self.num_of_vertices = 0
        self.dict_graph = {}

    def print_graph(self, title):
        print(title + "\n")
        for vertex, edges_lst in self.dict_graph.items():
            print(f"vertex: {vertex}")
            for edge in edges_lst:
                edge.print_edge()
            print("\n")


class Edge:
    def __init__(self, weight, overlap, next_vertex):
        self.weight = weight
        # TODO: pretty sure we don't need overlap
        self.overlap = overlap
        self.next_vertex = next_vertex

    def print_edge(self):
        print(f"next vertex: {self.next_vertex}, weight of edge: {self.weight}, overlap of edge: {self.overlap}")
