from collections import defaultdict
from server_api import is_open_position

class Graph:

    def __init__(self, maze):

        ## explored is the set of nodes in the graph for which we checked
        ## all possible edges that can contain that node
        self.explored = set()
        self.nodes = {}
        self.edges = defaultdict(set)
        self.maze = maze

    
    def add_edge(self, from_node, to_node):
        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)


    def add_node(self, node, is_free):
        self.nodes[node] = is_free


    def is_free(self, node):

        if (node not in self.nodes.keys()):
            return

        return self.nodes[node]


    def was_explored(self, node):
        return node in self.explored


    def mark_explored(self, node):
        self.explored.add(node)


    def explore_neighborhood(self, node, going_up):
        
        if (self.was_explored(node)):
            return

        if (is_open_position(node, self.maze.id)):

            self.add_node(node, is_free=True)
            
            x, y = node[0], node[1]
            node_right = (x + 1, y)
            node_left = (x - 1, y)
            node_up = (x, y + 1)
            node_down = (x, y - 1)

            if (going_up):

                if (x + 1 < self.maze.width and not self.was_explored(node_right)):
                    
                    check_free = is_open_position(node_right, self.maze.id)
                    self.add_node(node_right, is_free=check_free)
                    if (self.is_free(node_right)):
                        self.add_edge(node, node_right)

                if (y + 1 < self.maze.height and not self.was_explored(node_up)):
                    
                    check_free = is_open_position(node_up, self.maze.id)
                    self.add_node(node_up, is_free=check_free)
                    if (self.is_free(node_up)):
                        self.add_edge(node, node_up)

                if (x > 0 and not self.was_explored(node_left)):
                    
                    check_free = is_open_position(node_left, self.maze.id)
                    self.add_node(node_left, is_free=check_free)
                    if (self.is_free(node_left)):
                        self.add_edge(node, node_left)

                if (y > 0 and not self.was_explored(node_down)):

                    check_free = is_open_position(node_down, self.maze.id)
                    self.add_node(node_down, is_free=check_free)
                    if (self.is_free(node_down)):
                        self.add_edge(node, node_down)

            else:

                if (x > 0 and self.is_free(node_left)):
                    self.add_edge(node, node_left)

                if (y + 1 < self.maze.height and self.is_free(node_up)):
                    self.add_edge(node, node_up)

        else:
            self.add_node(node, is_free=False)


        self.mark_explored(node)

    
    ## BFS implementation from
    ## http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    def get_path(self, start, goal, maze_was_explored):

        queue = [(start, [start])]
        while queue:
            (node, path) = queue.pop(0)

            if (not maze_was_explored):
                self.explore_neighborhood(node, going_up=True)

            for next_node in set(self.edges[node]) - set(path):
                if (next_node == goal):
                    return path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))
