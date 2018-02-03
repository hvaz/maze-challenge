import json
import timeit
from maze import Maze
from server_api import get_maze

maze_info = get_maze()
if (maze_info == None):
    print 'Could not retrieve maze :('
    exit(1)

data = json.loads(maze_info)


def full_maze_solution():

    print 'Regular Maze..'
    print ''
    maze = Maze(data['width'], data['height'], data['id'])
    maze.leave_maze(explore_first=True)
    print ''


def optimal_maze_solution():
    print 'Maze Optimized..'
    print ''
    maze = Maze(data['width'], data['height'], data['id'])
    maze.leave_maze(explore_first=False)
    print ''


start_time = timeit.default_timer()
optimal_maze_solution()
elapsed = timeit.default_timer() - start_time
print "Time taken for OPTIMAL: {}".format(elapsed)

start_time = timeit.default_timer()
full_maze_solution()
elapsed = timeit.default_timer() - start_time
print "Time taken for REGULAR: {}".format(elapsed)
