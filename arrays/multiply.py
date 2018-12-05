def multiply(A, B):
    """
    Given two arrays A and B representing integers with one digit per array element,
    multiply the two integers and return the result as a new array.

     1 2
     1 2
    X___
     2 4
   1 2 0 +
   ______
   1 4 4

    """
    negative = True if (A[0] < 0) ^ (B[0] < 0) else False
    A[0] = abs(A[0])
    B[0] = abs(B[0])
    C = [0] * (len(A) + len(B))
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            C[i + j + 1] += A[i] * B[j]
            C[i + j] += C[i + j + 1] // 10
            C[i + j + 1] %= 10
    i = 0
    while i < len(C) - 1 and C[i] == 0: i += 1
    del C[:i]
    C[0] = -C[0] if negative else C[0]
    return C



print("Testing a lot of cases! Please wait!")
for i in range(0, 100):
    for j in range(0, 100):
        I = [int(x) for x in str(i)]
        J = [int(x) for x in str(j)]
        IJ = [int(x) for x in str(i * j)]
        assert multiply(I[:], J[:]) == IJ

assert multiply([-1, 0], [1, 0]) == [-1, 0, 0]
assert multiply([-1, 0], [-1, 0]) == [1, 0, 0]
assert multiply([-9, 9], [9, 9]) == [-9, 8, 0, 1]
