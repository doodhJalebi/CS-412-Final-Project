import timeit

mysetup = """
import numpy as np

# A = [[1,2],[4,5]]
# B = [[9,8],[6,5]]

A = np.random.randint(20, size=(128,128))
B = np.random.randint(20, size=(128,128))
n = 128
print("Initialization done.")
"""

mycode = """
ans = [[0 for y in range(n)] for x in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += A[i][k] * B[k][j]
    print(i)
print(ans)
"""

print(timeit.timeit(setup=mysetup, stmt=mycode, number=1))