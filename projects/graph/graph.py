"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import copy

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
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited=set()

        # Check if the node is visited
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
             # Print
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
           # Dequeue, the first PATH
           v = q.dequeue()
           # GRAB THE LAST VERTEX FROM THE PATH
           last_path = v[-1]
           # CHECK IF IT'S THE TARGET
           if last_path == destination_vertex:
               # IF SO, RETURN THE PATH
               return v
           # Check if it's been visited
           if last_path not in visited:
           # If it has not been visited...
               # Mark it as visited
               visited.add(last_path)
               # Then add A PATH TO all neighbors to the back of the queue
               for neighbor in self.get_neighbors(last_path):
                   # (Make a copy of the path before adding)
                v_copy = copy.copy(v)
                v_copy.append(neighbor)
                q.enqueue(v_copy)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create empty stack
        s = Stack()

        # add starting vertex path to stack
        s.push([starting_vertex])

        # Create an empty set to store visited nodes
        visited = set()

        # while stack is not empty
        while s.size() > 0:
            # pop last in path
            v = s.pop()
            # grab first vertex path
            last_path = v[-1]
            # check if it is the target
            if last_path == destination_vertex:
                # if so, return path
                return v
            # check if its been visited
            if last_path not in visited:
                # mark as visited
                visited.add(last_path)
                # Then add A PATH TO all neighbors to the front of the stack
                for neighbor in self.get_neighbors(last_path):
                    # make a copy of the path before adding
                    v_copy = copy.copy(v)
                    v_copy.append(neighbor)
                    s.push(v_copy)



    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited
        if visited is None:
            visited = set()

        # initialize path
        if path is None:
            path = []

        # check if starting vertex in visited
        if starting_vertex not in visited:
            # mark as visited
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)

            # if starting vertex is destination return
            if starting_vertex == destination_vertex:
                return path_copy

            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path

    
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("\n~~ BFT ~~\n")
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    print("\n~~ DFT ~~\n")
    graph.dft(1)
    print("\n~~ DFT Recursive ~~\n")
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print("\n~~ BFS ~~\n")
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print("\n~~ DFS ~~\n")
    print(graph.dfs(1, 6))
    print("\n~~ Recursive DFS ~~\n")
    print(graph.dfs_recursive(1, 6))
