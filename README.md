# Similar path generator.
generate similar path(s) of given path. Currently it can generate randomized nearly shortest path in 2D/3D. under development.

## Priority toward next node
The priority F(n) tells A* total moving cost from current node to adjacent nodes.
F(n) = g(n) + h(n)

## Cost function
The cost function can be used for node weight such as obstacles which is passable yet preferably to be avoided. 
Cost function and heuristic function need to be nomaralized.
When the cost function also takes noise the result path will be randomized.(such as random walk but towords the goal.)
