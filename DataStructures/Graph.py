class Queue:

    def __init__(self, items=None) -> None:
        if items is None:
            items = []
        self.queue: list = items

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        return self.queue


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

    def __getitem__(self, vertex_name):
        return self.vertices[vertex_name]


def breadth_first_search(graph: Graph, root):
    visited_vertices = list()
    graph_queue = Queue([root])
    visited_vertices.append(root)
    while len(graph_queue) > 0:
        node = graph_queue.dequeue()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.enqueue(elem)
    return visited_vertices


g = Graph()
a = Vertex("A")
b = Vertex("B")
g.add_vertex(a)
g.add_vertex(b)
g.add_edge(a.name, b.name)
g.print_graph()
print(breadth_first_search(g, 'A'))
