def delete_duplicates(A):
    """
    Given a sorted array A, remove all duplicates and return the result.
    The new empty indicies should be filled with a 0.

    1 0 0 2 0 0 3 0 0

    """
    # First pass: Set all duplicates to zero
    for i in reversed(range(1, len(A))):
        if A[i] == A[i - 1]:
            A[i] = 0
    # Second pass: Move all non-zero to front.
    swap_index = 0
    for i in range(len(A)):
        while swap_index < len(A) - 1 and A[swap_index] != 0:  # When would last condition happen
            swap_index += 1
        if A[i] and i > swap_index:
            A[i], A[swap_index] = A[swap_index], A[i]
    return A

assert delete_duplicates([1, 1, 2, 2]) == [1, 2, 0, 0]
assert delete_duplicates([1, 2, 3]) == [1, 2, 3]
assert delete_duplicates([1, 1, 1]) == [1, 0, 0]
assert delete_duplicates([1]) == [1]



