def next_permutation(A):
    """
    Given a permutation A, return the next permutation.

    e.g.  6 1 4 3 2 -> 6 2 4 3 1

    """
    i = len(A) - 2
    m = float('inf')
    m_pos = len(A) - 1
    while i > 0 and A[i] > A[i + 1]:
        if A[i + 1] < m:
            m = A[i + 1]
            m_pos = i + 1
        i -= 1
    if i == 0:
        return []
    A[i], A[m_pos] = A[m_pos], A[i]
    A[i + 1:] = list(sorted(A[i + 1:]))
    return A

def test():
    assert next_permutation([6, 1, 4, 3, 2]) == [6, 2, 1, 3, 4]
    assert next_permutation([4, 2, 3]) == [4, 3, 2]
    assert next_permutation([1, 0, 3, 2]) == [1, 2, 0, 3]
    assert next_permutation([1, 2, 3]) == [1, 3, 2]
    assert next_permutation([3, 2, 1]) == []
