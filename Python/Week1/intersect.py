import numpy as np

def on_segment(p1, p2, p3):
    """
    check whether p3 lies
    in the rectangle formed
    by point p1 and point p2
    """
    return True if (min(p1[0], p2[0]) <= p3[0] <= max(p1[0], p2[0])) and (min(p1[1], p2[1]) <= p3[1] <= max(p1[1], p2[1])) else False

def cross_product(p1, p2, p3):
    """
    cross product of vectors formed
    using three points p1, p2, p3
    with p1 as the origin.
    """
    p1, p2, p3 = np.array(p1), np.array(p2), np.array(p3)
    return np.cross(p3-p1, p2-p1)

def direction(p1, p2, p3):
    """
    clockwise or anticlockwise direction
    of vector p3p1 with respect to p1p2
    if cross product is postive
    """
    return cross_product(p1, p2, p3)
    
def segments_intersect(p1, p2, p3, p4):
    """
    check whether two segments p1p2, p3p4
    formed by the four points p1, p2, p3, p4
    on R^2 intersect or not.
    """
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(p3, p4, p1):
        return True
    elif d2 == 0 and on_segment(p3, p4, p2):
        return True
    elif d3 == 0 and on_segment(p1, p2, p3):
        return True
    elif d4 == 0 and on_segment(p1, p2, p4):
        return True
    else:
        return False

    