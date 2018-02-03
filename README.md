# maze-challenge

## Dependencies

The only dependency for running the code is the [requests](http://docs.python-requests.org/en/master/) python library. You can install it by running

```
pip install requests
```

## How to Run

To execute the code, simply run

```
python run_maze.py
```

## Labels

- '?' characters represent unexplored locations of the maze
- ' ' characters (blank spaces) represent explored locations of the maze that are free
- 'X' characters represent explored locations of the maze that are blocked by an obstacle
- '.' characters represent locations the are part of the exit path

## The Implementations

Both implementations rely on a Breadth First Search for finding a path between the maze's entrance and its exit. However, I chose to execute this algorithm in two different contexts.

### The OPTIMAL Maze

Under this context, we request maze information only as we need it. If our algorithm does not explore a certain set of nodes, there is no need in asking the server to tell us what is there at these places. You can visually observe this after the solution is printed to the screen: many locations will have the '?' character representing an unexplored location.

### The REGULAR Maze

Under this context, first we request information about the whole maze, and then we run the BFS algorithm. You can observer that after the solution is print to the screen there are no unexplored locations.

## Performance Comparison

The OPTIMAL maze implementation performs considerably better on average. The difference in performance increases as the maze dimensions increase, which is expected.

## Author

- Henrique Vaz
- hvaz@college.harvard.edu
- henriquevgvaz@gmail.com
