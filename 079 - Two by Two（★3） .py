


h,w = map(int,input().split())

A = []

for i in range(h):
    array = list(map(int, input().split()))
    A.append(array)

B = []

for i in range(h):
    array = list(map(int, input().split()))
    B.append(array)


tmp = 0
for i in range(h-1):
    for j in range(w-1):
        dif = B[i][j]-A[i][j]
        A[i][j]  +=dif
        A[i][j+1] += dif
        A[i+1][j] += dif
        A[i+1][j+1] += dif
        tmp += abs(dif) 

if A ==B:
    print("Yes")
    print(tmp)
else:
    print("No")