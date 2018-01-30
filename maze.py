from algorithms import Graph
from server_api import is_open_position

class Maze(object):

    def __init__(self, width, height, maze_id):
        if (width < 0 or height < 0):
            print 'Invalid maze dimensions'
            return None

        self.width = width
        self.height = height
        self.id = maze_id
        self.graph = Graph()


    def explore_maze(self):
        for y in range(self.height):
            for x in range(self.width):

                self.graph.add_node((x,y))

                if (is_open_position(x, y, self.id)):
                    self.graph.mark_free((x,y))


    def print_maze(self):
        print self.graph.free

        for y in range(self.height):
            for x in range(self.width):

                y_print = self.height - y - 1
                if ((x,y_print) in self.graph.free):
                    print ' ',
                else:
                    print 'X',

            print ''
