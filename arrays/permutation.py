def apply_permutation(A, P):
    """
    Given a permutation P = [p0, ..., pn]
    Apply the permutation to the array A.

    P = [2, 1, 0, 3]
    A = [1, 2, 3, 4]
    A' = [3, 2, 1, 4]

    """
    return [A[P[i]] for i in range(len(A))]

def test():
    assert apply_permutation([1, 2, 3, 4], [2, 1, 0, 3]) == [3, 2, 1, 4]

