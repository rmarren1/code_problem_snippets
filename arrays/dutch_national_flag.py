def dutch_national_flag(A, i):
    """
    Given an array A and an index i into A, order A into three groups where
    Group 1: All the values less than A[i]
    Group 2: All the values equal to A[i]
    Group 3: All the values greater than A[i]

    """
    pivot = A[i]
    less = 0
    curr = 0
    greater = len(A) - 1
    while curr <= greater:
        if A[curr] < pivot:
            A[less], A[curr] = A[curr], A[less]
            less += 1
            curr += 1
        elif A[curr] > pivot:
            A[greater], A[curr] = A[curr], A[greater]
            greater -= 1
        else:
            curr += 1

A = [9, 123, 4321, 1234, 88, 1, 0, -5, -2, -9, -15, 2000]
index = 4
pivot = A[index]
dutch_national_flag(A, index)
assert all(a < pivot for a in A[:A.index(pivot)])
assert all(a > pivot for a in A[A.index(pivot) + 1:])

A = [1,1,1,1,1,1,1]
B = A[:]
index = 2
pivot = A[index]
dutch_national_flag(A, index)
assert A == B
