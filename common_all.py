import math as m
import random as rnd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.patches import Rectangle

from copy import deepcopy

# ---

EXT_SIZE_X, EXT_SIZE_Y = 80, 60

INT_OFFS_X, INT_OFFS_Y = 20, 20
INT_SIZE_X, INT_SIZE_Y = 20, 20

EXT_BORDER = +300.0
INT_BORDER = +320.0

SOURCE_F0 = 60
SOURCE_BETA = 0.1
SOURCE_Y0 = 45
SOURCE_X0 = 9

STEP = 1


def func(y, x):
    # return 30
    src_yoff, src_xoff = y - SOURCE_Y0, x - SOURCE_X0
    src_off = src_yoff * src_yoff + src_xoff * src_xoff
    source = SOURCE_F0 * m.exp(-SOURCE_BETA * src_off)
    return source

K = 20

# ---

STEPS_1X = int(INT_OFFS_X / STEP)
STEPS_2X = int((INT_SIZE_X + 1) / STEP)
STEPS_3X = EXT_SIZE_X - INT_OFFS_X - INT_SIZE_X

STEPS_1Y = int(INT_OFFS_Y / STEP)
STEPS_2Y = int((INT_SIZE_Y + 1) / STEP)
STEPS_3Y = EXT_SIZE_Y - INT_OFFS_Y - INT_SIZE_Y

STEPS_X = STEPS_1X + STEPS_2X + STEPS_3X
STEPS_Y = STEPS_1Y + STEPS_2Y + STEPS_3Y

ibx0, iby0 = INT_OFFS_X, INT_OFFS_Y
ibx1, iby1 = INT_OFFS_X + INT_SIZE_X, INT_OFFS_Y + INT_SIZE_Y

# ---

USE_NUMBA = False

if USE_NUMBA:
    from numba import njit

def cond_jit():
    def decorator(func):
        if USE_NUMBA:
            return njit(func)
        else:
            return func

    return decorator