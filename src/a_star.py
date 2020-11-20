import collections
import heapq
import numpy as np
from utilities.util import profile_time, profile_args


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class SquareGrid:
    def __init__(self, width, height, barriers, depth=0):
        self.width = width
        self.height = height
        self.depth = depth
        self.barriers = barriers

    def in_bounds(self, coordinates):
        if self.depth == 0:
            (x, y) = coordinates
            return 0 <= x < self.width and 0 <= y < self.height
        elif self.depth <= 1:
            (x, y, z) = coordinates
            return 0 <= x < self.width and 0 <= y < self.height and 0 <= z < self.depth

    def passable(self, coordinates):
        return coordinates not in self.barriers

    def neighbors(self, coordinates):
        results = None
        if self.depth == 0:
            (x, y) = coordinates
            results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
            if (x + y) % 2 == 0: results.reverse()  # aesthetics

        elif self.depth <= 1:
            (x, y, z) = coordinates
            results = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


@profile_args
class GridWithWeights(SquareGrid):
    def __init__(self, width, height, barriers=None, obstacles=None):
        if obstacles is None:
            obstacles = {}
        if barriers is None:
            barriers = []
        super().__init__(width, height, barriers)
        self.weights = obstacles

    def cost(self, from_node, to_node, alpha=0):
        real_cost = 1 + alpha * (((self.weights.get(from_node, 1) + self.weights.get(to_node, 1)) / 2) - 1)
        noise = np.random.uniform(0, 1)  # gaussian distribution can be used here.
        return real_cost + noise

    def heuristic(self, v1, v2):
        # todo define L2 norm
        if self.depth == 0:
            (x1, y1) = v1
            (x2, y2) = v2
            return abs(x1 - x2) + abs(y1 - y2)
        elif self.depth <= 1:
            (x1, y1, z1) = v1
            (x2, y2, z2) = v2
            return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


@profile_time
def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next_node in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_node)
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + graph.heuristic(goal, next_node)
                frontier.put(next_node, priority)
                came_from[next_node] = current

    res = reconstruct_path(came_from, start, goal)

    return res
