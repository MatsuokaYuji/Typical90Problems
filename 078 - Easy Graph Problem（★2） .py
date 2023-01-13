#隣接行列O(N^2)か隣接リストO(M)



n,m = map(int,input().split())

list = [[] for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    list[a-1].append(b-1)
    list[b-1].append(a-1)

ans = 0

for i in range(n):
    tmp = 0
    for j in list[i]:
        if i>j:
            tmp+=1
    if tmp ==1:
        ans+=1
print(ans)
