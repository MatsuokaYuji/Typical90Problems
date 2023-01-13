



n = int(input())

s = input()

ans = 0

B = []

num = 0
for i in range(n):
    num += 1
    if i < n-1 and s[i] !=s[i+1]:
        B.append(num)
        num = 0
else:
    B.append(num)

tmp = 0

for i in range(len(B)):
    tmp += B[i] * (B[i] + 1) // 2
    
ans = n * (n+1)//2 - tmp

print(ans)
