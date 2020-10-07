# Similar path generator.
generate similar path(s) of given path. under development.

## Priority toward next node
The priority F(n) tells A* total moving cost from current node to adjacent nodes.
F(n) = g(n) + h(n)

## Cost function
The cost function can be used for node weight such as obstacles which is passable but prefer to avoid. 
Cost function and heuristic function need to be at the same scale.

## Heuristic function in A*
The heuristic function h(n) tells A* an estimate of the minimum cost from vertex n to the goal.
