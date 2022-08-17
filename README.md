# Similar path generator.
generate similar path(s) of given path. Currently it can generate randomized shortest(not promised) path in 2D/3D. under development.

## Problems of Random walk

## Priority toward next node
The priority F(n) tells A* total moving cost from current node to adjacent nodes.
F(n) = g(n) + h(n)

## Cost function
The cost function can be used for node weight such as obstacles which is passable but prefer to avoid. 
Cost function and heuristic function need to be at the same scale.
When the cost function also takes noise the result path will be randomized.(such as random walk but towords the goal.)

## Heuristic function in A*
The heuristic function h(n) tells A* an estimate of the minimum cost from vertex n to the goal.
