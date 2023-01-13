n,k = map(int,input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = True

diff = 0

#差分の絶対値を全て足す
for i in range(n):
    diff+=abs(a[i] - b[i])

if diff>k:
    flag = False
elif (k-diff)%2==1:
    flag = False



if flag:
    print("Yes")
else:
    print("No")

