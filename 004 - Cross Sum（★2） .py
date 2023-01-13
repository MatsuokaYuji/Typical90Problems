h,w = map(int, input().split())

A = []

for i in range(h):
    array = list(map(int, input().split()))
    A.append(array)


row = []
col = []

for i in range(h):
    tmp = 0
    for j in range(w):
        tmp +=A[i][j]
    row.append(tmp)


for j in range(w):
    tmp = 0
    for i in range(h):
        tmp +=A[i][j]
    col.append(tmp)

for i in range(h):
    B = []
    num = 0
    for j in range(w):
        num = row[i] + col[j] - A[i][j]
        B.append(str(num))
    ans = " ".join(B)
    print(ans)
    