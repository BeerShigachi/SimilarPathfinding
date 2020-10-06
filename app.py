
from src.a_star import GridWithWeights
from src.a_star import a_star_search
from src.grid import Grid

if __name__ == '__main__':
    # 2d
    space = (20, 20)  # coordinates wise

    # index wise
    start, goal = (0, 399)
    barriers = (2, 4)

    # {node(index):cost}
    obstacles = {12: 4, 14: 4, 31: 2}

    grid = Grid(spatial_size=space, barriers=barriers)
    graph = GridWithWeights(width=grid.x_axis, height=grid.y_axis, barriers=barriers, obstacles=obstacles)

    path = a_star_search(graph, start=grid.coordinates(start), goal=grid.coordinates(goal))
    print(path)



