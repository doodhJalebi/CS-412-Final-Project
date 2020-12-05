import numpy as np

A = np.random.randint(20, size=(4096,4096))
B = np.random.randint(20, size=(4096,4096))

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return (matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:])


def strassen(x, y, t):

    if len(x) == 1:
        return x * y

    a, b, c, d = split(x)
    e, f, g, h = split(y)

    p1 = strassen(a, f - h, t)
    p2 = strassen(a + b, h, t)
    p3 = strassen(c + d, e, t)
    p4 = strassen(d, g - e, t)
    p5 = strassen(a + d, e + h, t)
    p6 = strassen(b - d, g + h, t)
    p7 = strassen(a - c, e + f, t)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c

print(strassen(A,B,0))

