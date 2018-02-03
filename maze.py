import json
from algorithms import Graph
from server_api import submit_solution

wall = '*'
obstacle = 'X'
unexplored = '?'

class Maze(object):

    def __init__(self, width, height, maze_id):

        if (width < 0 or height < 0):
            print 'Invalid maze dimensions'
            return None

        self.width = width
        self.height = height
        self.id = maze_id
        self.graph = Graph(self)
        self.path_out = []


    def print_maze(self, explore_first):

        for i in range(self.width):
            print wall,
        print '  ' + wall

        for y in range(self.height):

            print wall,
            for x in range(self.width):

                node = (x, self.height - y - 1)
                if (explore_first):
                    self.graph.explore_neighborhood(node, going_up=False)

                if (self.graph.is_free(node)):
                    if (node in self.path_out):
                        print '.',
                    else:
                        print ' ',
                elif (self.graph.was_explored(node)):
                    print obstacle,
                else:
                    print unexplored,

            print wall
        
        print wall + '  ',
        for i in range(self.width):
            print wall,
        print ''


    def find_exit(self, explore_first):

        ## if not on_demand, print maze first
        if (explore_first):
            print 'Maze:'
            self.print_maze(explore_first)
            print ''

        return self.graph.get_path((0, 0), (self.width - 1, self.height - 1), explore_first)


    def leave_maze(self, explore_first):
       
        path_out = self.find_exit(explore_first)
        if (path_out == None):
            print 'No solution for maze... :('

        else:
            self.path_out = path_out
            print 'Maze Solution:'
            self.print_maze(explore_first=False)

        submit_solution(self.path_out, self.id)
