from common_all import *

def is_outside(y: float, x: float):
    if x <= 0 or x >= EXT_SIZE_X or y <= 0 or y >= EXT_SIZE_Y:
        return True
    if ibx0 <= x <= ibx1 and iby0 <= y <= iby1:
        return True
    return False

def dist_pt_segm_hor(ptx: int, pty: int, sx1: int, sx2: int, sy: int):
    # assert sx1 < sx2
    if ptx < sx1:
        return m.hypot(sx1 - ptx, abs(pty - sy))
    elif ptx > sx2:
        return m.hypot(ptx - sx2, abs(pty - sy))
    else:
        return abs(pty - sy)

def dist_pt_segm_vert(ptx: int, pty: int, sy1: int, sy2: int, sx: int):
    return dist_pt_segm_hor(pty, ptx, sy1, sy2, sx)

_VERT_PART_SEP = INT_OFFS_Y + INT_SIZE_Y / 2
_HOR_PART_SEP = INT_OFFS_X + INT_SIZE_X / 2

# Assumed that point is valid
def dist_to_border(y: int, x: int):
    min_ext, min_int = m.inf, m.inf

    if y < _VERT_PART_SEP:  # Top part
        min_ext = dist_pt_segm_hor(x, y, 0, EXT_SIZE_X, 0)  # Ext top
        min_int = dist_pt_segm_hor(x, y, ibx0, ibx1, iby0)  # Int top
    else:  # Bottom part
        min_ext = dist_pt_segm_hor(x, y, 0, EXT_SIZE_X, EXT_SIZE_Y)  # Ext bottom
        min_int = dist_pt_segm_hor(x, y, ibx0, ibx1, iby1)  # Int bottom

    if x < _HOR_PART_SEP:  # Left part
        min_ext = min(min_ext, dist_pt_segm_vert(x, y, 0, EXT_SIZE_Y, 0))  # Ext left
        min_int = min(min_int, dist_pt_segm_vert(x, y, iby0, iby1, ibx0))  # Int left
    else:
        min_ext = min(min_ext, dist_pt_segm_vert(x, y, 0, EXT_SIZE_Y, EXT_SIZE_X))  # Ext right
        min_int = min(min_int, dist_pt_segm_vert(x, y, iby0, iby1, ibx1))  # Int right

    if min_ext < min_int:
        return min_ext, EXT_BORDER  # TODO: Non constant temperature
    else:
        return min_int, INT_BORDER
