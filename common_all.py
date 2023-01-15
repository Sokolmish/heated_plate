import math as m
import random as rnd
import numpy as np
import statistics as st

from copy import deepcopy

import matplotlib.pyplot as plt
import matplotlib

# plt.style.use('seaborn-whitegrid')
# matplotlib.rc('xtick', labelsize=14) 
# matplotlib.rc('ytick', labelsize=14) 

# ---

EXT_SIZE_X, EXT_SIZE_Y = 160, 120

INT_OFFS_X, INT_OFFS_Y = 40, 40
INT_SIZE_X, INT_SIZE_Y = 40, 40

EXT_BORDER = +300.0
INT_BORDER = +330.0  # 330

SOURCE_F0 = 70
SOURCE_BETA = 0.1
SOURCE_X0 = 100
SOURCE_Y0 = 25

PASSIVE_HEATING = 0

STEP = 1


def func(y, x):
    # return 30
    src_yoff, src_xoff = y - SOURCE_Y0, x - SOURCE_X0
    src_off = src_yoff * src_yoff + src_xoff * src_xoff
    source = SOURCE_F0 * m.exp(-SOURCE_BETA * src_off)
    return source + PASSIVE_HEATING

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

K_SIN_SCALE = 0.1

def k_func(y, x):
    return 5 * (m.sin(K_SIN_SCALE * x) + m.sin(K_SIN_SCALE * y)) + K
    # return 20

ktbl = np.zeros((STEPS_Y, STEPS_X), dtype=float)
kdx = np.zeros((STEPS_Y, STEPS_X), dtype=float)
kdy = np.zeros((STEPS_Y, STEPS_X), dtype=float)

for j in range(1, STEPS_Y - 1):
    for i in range(1, STEPS_X - 1):
        ktbl[j, i] = k_func(j * STEP, i * STEP)
        kdx[j, i] = K_SIN_SCALE * m.cos(i * STEP)
        kdy[j, i] = K_SIN_SCALE * m.cos(j * STEP)


# ---

def lerp(x, y, t):
    return (1 - t) * x + t * y

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