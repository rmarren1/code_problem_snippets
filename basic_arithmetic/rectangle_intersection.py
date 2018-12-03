def rectangle_intersection(A, B):
    """
    Given two rectangles A, B, return the intersection if there is one.

    A triangle is represented by a 4-tuple (x0, x1, y0, y1)
    x0---------x1 -y1
    |          |   |
    |          |   |
    |          |   |
    +----------+ --y0
    """
    # Test if there is an X axis intersection
    rightmost_left_x = max(A[0], B[0])
    leftmost_right_x = min(A[1], B[1])
    topmost_lower_y = max(A[2], B[2])
    downmost_upper_y = min(A[3], B[3])
    if rightmost_left_x < leftmost_right_x and topmost_lower_y < downmost_upper_y:
        return (rightmost_left_x, leftmost_right_x, topmost_lower_y, downmost_upper_y)
    return False

assert     rectangle_intersection((1, 4, 2, 6), (3, 5, 4, 10)) == (3, 4, 4, 6)
assert     rectangle_intersection((-1, 1, -1, 1), (-2, 2, -2, 2)) == (-1, 1, -1, 1)
assert not rectangle_intersection((1, 4, 2, 6), (5, 10, 7, 10))
