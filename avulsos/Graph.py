class Vertex:
    def __init__(self, name = "", value = None):
        self.name = name
        self.value = value

class Edge:
    def __init__(self,vertex1,vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2

class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        for edge in edges:
            if not (edge.vertex1 in vertices): raise("Vertex {} not in vertices list.".format(edge.vertex1))
            if not (edge.vertex2 in vertices): raise("Vertex {} not in vertices list.".format(edge.vertex2))
        self.edges = edges
