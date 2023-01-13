
# PyPyで出すとAC、再起関数以外は基本pypyでよさそう
n,p,q = map(int,input().split())

A = list(map(int, input().split()))

ans = 0
for i in range(n-4):
    for j in range(i+1,n-3):
        for k in range(j+1,n-2):
            for l in range(k+1,n-1):
                for m in range(l+1,n):
                    if A[i] * A[j]%p * A[k]%p * A[l]%p * A[m]%p == q:
                        ans+=1

print(ans)
