from util import Queue, Stack


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):

    # create graph
    graph = Graph()

    # create array of vertices
    vertices_with_dups = [item for t in ancestors for item in t]
    vertices = list(dict.fromkeys(vertices_with_dups))

    # loop through and add each vertex
    for vertex in vertices:
        graph.add_vertex(vertex)

    # loop through and add each edge
    for ancestor in ancestors:
        graph.add_edge(ancestor[0], ancestor[1])

    # create empty stack
    s = Stack()

    # push starting vertex into stack
    s.push(starting_node)

    # route to final ancestor
    route = []

    # create an empty set to store visited nodes
    visited = set()

    # while the stack is not empty
    while s.size() > 0:
        # pop the first vertex
        v = s.pop()
        # check if visited and if not, mark as visited
        if v not in visited:
            # mark as visited
            visited.add(v)
            # add to route
            route.append(v)
            # then push all neighbors to the top of the stack
            for neighbor in graph.get_neighbors(v):
                s.push(neighbor)

    return route[-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 7))
