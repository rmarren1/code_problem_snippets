def can_advance(A):
    """
    Given an array A of integers A, treat each integet A[i] in A as the number of
    indices forward in A you can move.

    For example, if A = [2, 0, 3], you can move:
    2 spaces starting from index 0
    0 spaces starting from index 1
    1 space  starting from index 2

    return whether or not you can move to the end of the array.

    0 1 2 3
    2 0 1 0

    """
    last_position = len(A) - 1
    num_elements = len(A)
    if num_elements == 1 and A[0] > 0:
        return True
    for i in range(1, num_elements):
        if A[last_position - i] >= i:
            if can_advance(A[:last_position - i + 1]):
                return True
    return False

assert     can_advance([2, 0, 1, 1])
assert     can_advance([2])
assert     can_advance([10, 0, 0, 0, 0, 0])
assert     can_advance([1, 1, 1, 1, 1, 1])
assert     can_advance([2, 0, 2, 0, 2, 0])
assert not can_advance([2, 0, 0, 1])
assert not can_advance([0, 6, 0, 1])
assert not can_advance([0])
assert not can_advance([0] + [5, 4, 3, 2, 1] * 100)
