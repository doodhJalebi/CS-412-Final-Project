import numpy as np

A = np.random.randint(20, size=(4096,4096))
B = np.random.randint(20, size=(4096,4096))
n = 4096

ans = [[0 for y in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += A[i][k] * B[k][j]

print(ans)

