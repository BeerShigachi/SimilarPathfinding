
from src.a_star import GridWithWeights
from src.a_star import a_star_search
from src.grid import Grid

if __name__ == '__main__':
    # 2d
    space = (20, 20)  # coordinates wise

    # index wise
    start, goal = (21, 200)
    obs = (2, 4)

    grid = Grid(spatial_size=space, obstacles=obs)
    graph = GridWithWeights(width=grid.x_axis, height=grid.y_axis)

    res = a_star_search(graph, start=grid.coordinates(start), goal=grid.coordinates(goal))

    print(res)

