# 制約から解法を予測

import itertools


n = int(input())

A = []

for i in range(n):
    array = list(map(int,input().split()))
    A.append(array)

m = int(input())

disc = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    x,y = map(int,input().split())
    disc[x-1][y-1] = 1
    disc[y-1][x-1] = 1
# イメージ [[0, 1, 0], [1, 0, 0], [0, 0, 0]]

per_list = list(itertools.permutations(range(n)))
# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

# 仮の最大値
ans = int(1e9)
flag = False
# for i in range(n):

for i in per_list:
    tmp = 0
    for j in range(n):
        if j < n-1 and disc[i[j]][i[j+1]] == 1:
            break
        tmp += A[i[j]][j]
    else:
        ans = min(ans,tmp)
        flag = True
if flag:
    print(ans)
else:
    print(-1)
