


# 上階を見積もる
n,k = map(int,input().split())

score = []

for i in range(n):
    a,b = map(int,input().split())
    score.append(a-b)
    score.append(b)

score.sort(reverse=True)

ans = 0

for i in range(k):
    ans+=score[i]
print(ans)