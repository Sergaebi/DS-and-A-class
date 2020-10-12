class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbours = set()

    def add_neighbour(self, vertex):
        self.neighbours.add(vertex)


class Graph:

    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add_neighbour(vertex2)
            self.vertices[vertex2].add_neighbour(vertex1)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbours)))


g = Graph()
a = Vertex("A")
b = Vertex("B")
g.add_vertex(a)
g.add_vertex(b)
g.add_edge(a.name, b.name)
g.print_graph()
