import timeit


mysetup = """
import numpy as np

# A = np.matrix([[1,2],[4,5]])
# B = np.matrix([[9,8],[6,5]])

A = np.random.randint(20, size=(128,128))
B = np.random.randint(20, size=(128,128))

print("Initialization done.")

def split(matrix):
    # print("Splitting...")
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return (matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:])


def strassen(x, y, t):
    # print("Strassening...")
    
    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y

    # Splitting the matrices into quadrants. This will be done recursively
    # untill the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)

    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen(a, f - h, t)
    p2 = strassen(a + b, h, t)
    p3 = strassen(c + d, e, t)
    p4 = strassen(d, g - e, t)
    p5 = strassen(a + d, e + h, t)
    p6 = strassen(b - d, g + h, t)
    p7 = strassen(a - c, e + f, t)

    # print("Combining...")

    # Computing the values of the 4 quadrants of the final matrix c
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c
"""

mycode = """
print(strassen(A,B,0))
"""
print(timeit.timeit(setup=mysetup, stmt=mycode, number=1))