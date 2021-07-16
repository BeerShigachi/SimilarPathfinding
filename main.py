
from src.a_star import GridWithWeights
from src.a_star import a_star_search
from src.grid import Grid

if __name__ == '__main__':
    # 2d
    space = (20, 20)  # coordinates wise

    # 3d
    # space = (20, 20, 5)  # coordinates wise

    # index wise
    start, goal = (0, 350)

    # constraints. you cannot pass.
    barriers = (2, 4)

    # todo implement algorithm to define a similarity.
    #  similarity = high, low, etc...

    # {node(index):cost}
    obstacles = {12: 4, 14: 4, 31: 2}

    grid = Grid(spatial_size=space, barriers=barriers)
    graph = GridWithWeights(grid=grid, obstacles=obstacles)

    path = a_star_search(graph, start=grid.coordinates(start), goal=grid.coordinates(goal), relays=[])
    res = [grid.decimal(v) for v in path]

    print(res)


