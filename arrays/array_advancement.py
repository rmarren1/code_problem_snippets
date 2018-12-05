def can_advance(A):
    """
    Given an array A of integers A, treat each integet A[i] in A as the number of
    indices forward in A you can move.

    For example, if A = [2, 0, 3], you can move:
    2 spaces starting from index 0
    0 spaces starting from index 1
    1 space  starting from index 2

    return whether or not you can move to the end of the array.

    visited = set()
    queue = [0]
    while queue:
        curr = queue.pop()
        visited.add(curr)
        for i in range(curr, curr + A[curr]):
            if i not in visited and i < len(A):
                queue.insert(0, A[i])
    return (len(A) - 1) in visited


    2 0 3 0 0 4 1 2 3 4 
    X X X 0 0 0 0 0 0 0
    """
    visited = set()
    queue = [0] if A[0] else []
    while queue:
        curr = queue.pop()
        visited.add(curr)
        for i in range(curr + 1, curr + 1 + A[curr]):
            if i not in visited and i < len(A):
                queue.insert(0, i)
    return (len(A) - 1) in visited

assert     can_advance([2, 0, 1, 1])
assert     can_advance([2])
assert     can_advance([10, 0, 0, 0, 0, 0])
assert     can_advance([1, 1, 1, 1, 1, 1])
assert     can_advance([2, 0, 2, 0, 2, 0])
assert not can_advance([2, 0, 0, 1])
assert not can_advance([0, 6, 0, 1])
assert not can_advance([0])
assert not can_advance([0] + [5, 4, 3, 2, 1] * 100)
