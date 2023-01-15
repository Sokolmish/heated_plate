import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Rectangle


class MeshResult:
    def __init__(self, mesh: np.ndarray, iters: int, time: float) -> None:
        self.mesh = mesh
        self.iters = iters
        self.time = time

        self.y = None
        self.x = None
        self.szy = None
        self.szx = None

    # (INT_OFFS_Y, INT_OFFS_X), INT_SIZE_Y, INT_SIZE_X
    def set_hole(self, y, x, szy, szx) -> None:
        self.y = y
        self.x = x
        self.szy = szy
        self.szx = szx

    def value_at(self, x, y):
        return self.mesh[y, x]

    def show_heatmap(self) -> None:
        vmin = min(min(x for x in row if x > 1e-3) for row in self.mesh)
        plt.imshow(self.mesh, cmap=cm.plasma, vmin=vmin)
        hole_rect = Rectangle((self.y, self.x), self.szy, self.szx,
                              edgecolor='black', facecolor='white')
        plt.gca().add_patch(hole_rect)
        plt.colorbar()
        plt.show()


class PointResult:
    def __init__(self, res: float, avg_hops: int, time: float) -> None:
        self.res = res
        self.avg_hops = avg_hops
        self.time = time

