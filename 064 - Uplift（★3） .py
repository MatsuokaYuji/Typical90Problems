from re import L


n,q = map(int,input().split())

A = list(map(int, input().split()))

L = []

R = []

V = []

for i in range(q):
    l,r,v = map(int,input().split())
    L.append(l-1)
    R.append(r-1)
    V.append(v)

# print(L,R,V)
# [2, 1, 1] [3, 2, 3] [1, -1, 2]
# 累積和
ans = 0
B = []
for i in range(n-1):
    B.append(A[i+1]-A[i])
    ans+= abs(B[i])
else:
    B.append(0)

for i in range(q):
    before = abs(B[L[i]-1]) + abs(B[R[i]])
    if L[i] >= 1:
        B[L[i]-1] += V[i]
    if R[i] <= n-2:
        B[R[i]] -= V[i]
    after = abs(B[L[i]-1]) + abs(B[R[i]])
    ans += after - before
    print(ans)

