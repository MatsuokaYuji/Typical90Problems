# O(logN)O(log⁡N) 	O(N)O(N)	O(N2)O(N2)	O(N3)O(N3)	O(2N)O(2N)
# 何でもあり	10^8 程度	10000 ～ 20000 程度	400 ～ 600 程度	20 ～ 25 程度

n, l = map(int,input().split())

k = int(input())

A = list(map(int, input().split()))


# すべてx以上の長さで切れるか判定
def afterdark(x):
    #切った個数
    cnt = 0
    #最後に切った位置
    last = 0
    for i in range(n):
        if A[i] - last >= x and l - A[i] >= x:
            cnt+=1
            last = A[i]
    if cnt >= k:
        return True
    else:
        return False

# 二分探索で最も短い長さを探索
left = 0
right = l

while abs(left - right)>1:
    mid = (left + right)//2
    if afterdark(mid):
        left = mid
    else:
        right = mid
print(left)
