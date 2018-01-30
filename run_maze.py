import json
from maze import Maze
from server_api import get_maze

maze_info = get_maze()
if (maze_info == None):
    print 'Could not retrieve maze :('
    exit(1)

data = json.loads(maze_info)

maze = Maze(data['width'], data['height'], data['id'])
maze.explore_maze()
maze.print_maze()
