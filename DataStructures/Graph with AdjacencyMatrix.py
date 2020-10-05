class Vertex:

    def __init__(self, name):
        self.name = name


class Graph:

    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        return False

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.edges[self.edge_indices[vertex1]][self.edge_indices[vertex2]] = weight
            self.edges[self.edge_indices[vertex2]][self.edge_indices[vertex1]] = weight
            return True
        return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + " ", end="")
            for j in range(len(self.edges)):
                print(self.edges[i][j], end=" ")
            print(" ")
