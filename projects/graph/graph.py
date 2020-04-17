"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # print(" this is bft")
        qq = Queue()
        qq.enqueue(starting_vertex)
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            v = qq.dequeue()
            # if not visited
            if v not in visited:
                # DO THE THING!!!!!!!
                print(v)
                # mark as visited
                visited.add(v)
                # enqueue all neightbors
                for neighbor in self.get_neighbors(v):
                    qq.enqueue(neighbor)
        # print("end of bft", print(visited))

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # print(" this is Dft")
        # create stack
        s = Stack()
        # start vertex
        s.push(starting_vertex)
        # create a set to store visited vertices
        visited = set()
        # while  stack is not empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # check if it's been visited
            if v not in visited:
                # mark if visited
                print(v)
                visited.add(v)
                # push all its neighbors into stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

        # print(" this is end of Dft", visited)
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create stack

        # check if visited is empty that way you dont create something each rec
        if visited == None:
            # s = Stack()
            # s.push(starting_vertex)
            visited = set()

        print(starting_vertex)
        # add starting node
        visited.add(starting_vertex)

        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                self.dft_recursive(n, visited)

        # check if the node has been visited
        # if not
            # mark it as visited
            # call dft_recursive on each neighbor

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # print("this is BFS")
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue the first vertex
            path = qq.dequeue()
            v = path[-1]
            # check if it is visited
            # if not visited
            if v not in visited:

                # check if target
                # if so, return path
                if v == destination_vertex:
                    return path
                    # mark as visited
                visited.add(v)
            # enqueue all neighbors
                for neighbor in self.get_neighbors(v):
                    # qq.enqueue(neighbor)
                    # make a copy of the path

                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    qq.enqueue(path_copy)

                # enqueue the copy

        # print("end of bfs")

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
    # print(" this is Dft")

        if starting_vertex == destination_vertex:
            return [starting_vertex]
        # create stack
        s = Stack()
        # start vertex
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while  stack is not empty
        while s.size() > 0:
            # pop the first vertex
            path = s.pop()
            v = path[-1]
            # check if it's been visited
            if v not in visited:
                # mark if visited
                if v == destination_vertex:
                    return path
              
                visited.add(v)
                # push all its neighbors into stack
                for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)

        # print(" this is end of Dft", visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path =None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print("dfs_rec afaaf")
        # check if visited is empty that way you dont create something each rec
        if visited == None:
            # s = Stack()
            # s.push(starting_vertex)
            visited = set()
        # check if path is empty that way you dont create something each rec
        if path == None:
            path = []
        #add start node
        visited.add(starting_vertex)
        #add path node
        # path = path + [starting_vertex]
        path_copy = path.copy()
        path_copy.append(starting_vertex)
        #check for destination
        if starting_vertex == destination_vertex:
            return path_copy
     
        else: 
            #look through neighbors and rec each neighbor and update the path     
            
            for n in self.get_neighbors(starting_vertex):
                if n not in visited:
                   
                    new_path = self.dfs_recursive(n, destination_vertex, visited, path_copy)

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
