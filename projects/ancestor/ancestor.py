# The input will not be empty.
# There are no cycles in the input.
# There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# IDs will always be positive integers.
# A parent may have any number of children.

#graph problem
#need a Bfs
#import utls
#bring bfs over and graph stuff
#change dfs so it checks for the longest path to find the oldest ancestor
from util import Stack, Queue 


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        

    def add_edges(self, v1, v2):
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

def earliest_ancestor(ancestors, starting_node):
    #build a graph
    graph = Graph()

    #loop ancestors to add to graph
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # build the edges
        graph.add_edges(pair[1], pair[0])

    qq = Queue()
    qq.enqueue( [starting_node ])
    max_path =1
    oldest_ancestor = -1
        # While queue is not empty:
    while qq.size() > 0:
        # dequeue the first vertex
        path = qq.dequeue()
        v = path[-1]
        # check if it is visited
        # if not visited
        #check the len to find the longest path and also check the value if there is a tie
        if(len(path) >= max_path and v < oldest_ancestor) or (len(path) > max_path):
            oldest_ancestor = v
            max_path = len(path)

        # enqueue all neighbors
        for neighbor in graph.vertices[v]:
            # qq.enqueue(neighbor)
            # make a copy of the path

            path_copy = list(path)
            path_copy.append(neighbor)
            qq.enqueue(path_copy)

            # enqueue the copy
    return oldest_ancestor