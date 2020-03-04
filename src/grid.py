
import numpy as np


class Grid:
    def __init__(self, spatial_size, obstacles=()):
        self.dimension = len(spatial_size)
        if self.dimension == 3:
            self.x_axis = spatial_size[0]
            self.y_axis = spatial_size[1]
            self.z_axis = spatial_size[2]
            self.grid_size = self.x_axis * self.y_axis * self.z_axis
            self.occupancy = np.zeros([self.x_axis, self.y_axis, self.z_axis], dtype=np.uint8)
        elif self.dimension == 2:
            self.x_axis = spatial_size[0]
            self.y_axis = spatial_size[1]
            self.grid_size = self.x_axis * self.y_axis
            self.occupancy = np.zeros([self.x_axis, self.y_axis], dtype=np.uint8)
        else:
            raise ValueError('spatial_size must be 2 or 3 dimension.')
        for o in obstacles:
            self.occupy(o)

        # self.nodes = self.all_nodes()

    def coordinates(self, v):
        if v < 0 or v > self.grid_size:
            return -1
        if self.dimension == 3:
            x = v // (self.y_axis * self.z_axis)
            y = (v // self.z_axis) % self.y_axis
            z = v % self.z_axis
            return x, y, z
        elif self.dimension == 2:
            x = v // self.y_axis
            y = v % self.y_axis
            return x, y
        else:
            return -1

    def decimal(self, v):
        if v[0] < 0 or v[0] > self.x_axis or v[1] < 0 or v[1] > self.y_axis or v[2] < 0 or v[2] > self.z_axis:
            return -1
        if self.dimension == 3:
            return v[0] * (self.y_axis * self.z_axis) + v[1] * self.z_axis + v[2]
        elif self.dimension == 2:
            return v[0] * self.y_axis + 1
        else:
            return -1

    def occupy(self, *args):
        for v in args:
            self.occupancy[self.coordinates(v)] = -1

    def is_vacant(self, v):
        return self.occupancy[self.coordinates(v)] == 0

    def neighbors(self, v):
        ls = []
        _v = self.coordinates(v)
        if self.dimension == 2:
            if _v[0] != 0:
                x_neighbor = v - self.y_axis
                if self.is_vacant(x_neighbor):
                    ls.append(x_neighbor)
            if _v[0] != self.x_axis - 1:
                x_neighbor = v + self.y_axis
                if self.is_vacant(x_neighbor):
                    ls.append(x_neighbor)

            if _v[1] != 0:
                y_neighbor = v - 1
                if self.is_vacant(y_neighbor):
                    ls.append(y_neighbor)
            if _v[1] != self.y_axis - 1:
                y_neighbor = v + 1
                if self.is_vacant(y_neighbor):
                    ls.append(y_neighbor)

        elif self.dimension == 3:
            if _v[0] != 0:
                x_neighbor = v - (self.y_axis * self.z_axis)
                if self.is_vacant(x_neighbor):
                    ls.append(x_neighbor)
            if _v[0] != self.x_axis - 1:
                x_neighbor = v + (self.y_axis * self.z_axis)
                if self.is_vacant(x_neighbor):
                    ls.append(x_neighbor)

            if _v[1] != 0:
                y_neighbor = v - self.z_axis
                if self.is_vacant(y_neighbor):
                    ls.append(y_neighbor)
            if _v[1] != self.y_axis - 1:
                y_neighbor = v + self.z_axis
                if self.is_vacant(y_neighbor):
                    ls.append(y_neighbor)

            if _v[2] != 0:
                z_neighbor = v - 1
                if self.is_vacant(z_neighbor):
                    ls.append(z_neighbor)
            if _v[2] != self.z_axis - 1:
                z_neighbor = v + 1
                if self.is_vacant(z_neighbor):
                    ls.append(z_neighbor)
        return ls

    def manhattan_dist(self, v1, v2):
        s1 = np.array(self.coordinates(v1))
        s2 = np.array(self.coordinates(v2))
        return np.linalg.norm(s1 - s2, 1)

    def euclidean_dist(self, v1, v2):
        s1 = np.array(self.coordinates(v1))
        s2 = np.array(self.coordinates(v2))
        return np.linalg.norm(s1 - s2, 2)


g = Grid((8, 8), obstacles=(2, 0, 9))
print(g.euclidean_dist(3, 21))
# def all_nodes(self):
#     nodes = []
#     for i in range(self.x_axis):
#         for j in range(self.y_axis):
#             for k in range(self.z_axis):
#                 nodes.append(np.array([i, j, k]))
#
#     return nodes

# def neighbor(self, node):
#     direction = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1]), np.array([-1, 0, 0]),
#                  np.array([0, -1, 0]), np.array([0, 0, -1])]
#     res = []
#     for d in direction:
#         res.append(node + d)
#     return res
