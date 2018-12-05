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
    m = A if len(A) <= len(B) else B
    M = A if len(A) > len(B) else B
    s = [0] * (len(m) + len(M))
    m.reverse()
    M.reverse()
    for i in range(len(m)):
        for j in range(len(M)):
            s[i + j] += m[i] * M[j]
    for i in range(len(s) - 1):
        tmp = s[i]
        s[i] = tmp % 10
        s[i + 1] += tmp // 10
    s.reverse()
    i = 0
    while i < len(s) - 1 and s[i] == 0: i += 1
    del s[:i]
    return s

print("Testing a lot of cases! Please wait!")
for i in range(1000):
    for j in range(1000):
        I = [int(x) for x in str(i)]
        J = [int(x) for x in str(j)]
        IJ = [int(x) for x in str(i * j)]
        assert multiply(I[:], J[:]) == IJ


