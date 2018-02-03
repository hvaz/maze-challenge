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
- '.' characters represent locations that are part of the exit path

## The Implementations

Both implementations rely on a Breadth First Search for finding a path between the maze's entrance and its exit. However, I chose to execute this algorithm in two different contexts.

### The OPTIMAL Maze

Under this context, we request maze information only as we need it. If our algorithm does not explore a certain set of nodes, there is no need in asking the server to tell us what is there at these places. You can visually observe this after the solution is printed to the screen: many locations will have the '?' character representing an unexplored location.

### The REGULAR Maze

Under this context, first we request information about the whole maze, and then we run the BFS algorithm. You can observer that after the solution is print to the screen there are no unexplored locations.

## Performance Comparison

The OPTIMAL maze implementation performs considerably better on average. The difference in performance increases as the maze dimensions increase, which is expected.

## Example Output

```
➜  maze-challenge git:(master) ✗ python run_maze.py
{"height":18,"id":"f1dae6addabecdf255cbffcf425d276dda75d5ab6fcbb55f27ad5db9bad592e5adafdeb61cfabd6bf","width":18}
Maze Optimized..

Maze Solution:
* * * * * * * * * * * * * * * * * *   *
* ? ? ? ? ? ? ?     ?   ? . . . . . . *
* ? ? ? ? ? ? ? ?         . ?   ?   ? *
* ? ? ? ? ? ? ?     ?   ? .   ? ? ? ? *
* ? ? ? ? ? ? ? ?   ? ?   . ? ? ? ? ? *
* ? ? ? ? ? ? ? ? ? ? ? ? . ? ? ? ? ? *
* ? ? ? ? ? ? ?     ?   . . ? ? ? ? ? *
* ? ? ? ? ? ?     ?   ? . ? ? ? ? ? ? *
* ? ? ?   ?   ? . . . . . ? ? ? ? ? ? *
*   ?   . . . . . ? ?   ? ? ? ? ? ? ? *
*     ? . ?   ?     ?   ? ? ? ? ? ? ? *
* ?     . ?     ?   ? ? ? ? ? ? ? ? ? *
*     ? . ? ?   ? ? ? ? ? ? ? ? ? ? ? *
* ? ?   . .   ? ? ? ? ? ? ? ? ? ? ? ? *
*     ? ? . ? ? ? ? ? ? ? ? ? ? ? ? ? *
* ?       .   ? ? ? ? ? ? ? ? ? ? ? ? *
*   ?   ? . ? ? ? ? ? ? ? ? ? ? ? ? ? *
*   ? ? . . ? ? ? ? ? ? ? ? ? ? ? ? ? *
* . . . . ? ? ? ? ? ? ? ? ? ? ? ? ? ? *
*   * * * * * * * * * * * * * * * * * *
Solution for maze is correct!
Correct solution!

Time taken for OPTIMAL: 63.9566619396
Regular Maze..

Maze:
* * * * * * * * * * * * * * * * * *   *
*         X   X     X   X             *
* X X X       X X           X   X   X *
*         X         X   X     X     X *
* X   X     X   X     X     X   X     *
* X   X   X     X X   X X   X       X *
*   X       X X     X       X   X     *
*       X   X     X   X   X       X   *
* X   X   X   X           X X   X X   *
*   X             X X   X       X     *
*     X   X   X     X   X   X     X   *
* X       X     X   X X       X   X   *
*     X   X X   X X       X     X     *
* X X         X   X X X X   X X   X   *
*     X X   X                         *
* X           X X   X X   X   X   X   *
*   X   X   X           X     X X     *
*   X X     X   X   X     X       X   *
*         X X X       X     X   X     *
*   * * * * * * * * * * * * * * * * * *

Maze Solution:
* * * * * * * * * * * * * * * * * *   *
*         X   X     X   X . . . . . . *
* X X X       X X         . X   X   X *
*         X         X   X .   X     X *
* X   X     X   X     X   . X   X     *
* X   X   X     X X   X X . X       X *
*   X       X X     X   . . X   X     *
*       X   X     X   X . X       X   *
* X   X   X   X . . . . . X X   X X   *
*   X   . . . . . X X   X       X     *
*     X . X   X     X   X   X     X   *
* X     . X     X   X X       X   X   *
*     X . X X   X X       X     X     *
* X X   . .   X   X X X X   X X   X   *
*     X X . X                         *
* X       .   X X   X X   X   X   X   *
*   X   X . X           X     X X     *
*   X X . . X   X   X     X       X   *
* . . . . X X X       X     X   X     *
*   * * * * * * * * * * * * * * * * * *
Solution for maze is correct!
Correct solution!

Time taken for REGULAR: 66.071158886
```

## Further Work

In order to make this implementation more "professional", one could write a small bash script that define important environment variables, such as the server address, which as of now is hard coded. 
One could also make small changes in the code to allow the user to run only one of the two implementations, or both.

## Author

- Henrique Vaz
- hvaz@college.harvard.edu
- henriquevgvaz@gmail.com
