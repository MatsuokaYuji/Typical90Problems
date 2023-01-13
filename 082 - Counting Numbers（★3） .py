

L, R = input().split()
li = int(L)
ri = int(R)
ll = len(L)
lr = len(R)
t = 0
MOD = 10 ** 9 + 7
for i in range(ll, lr + 1):
    ts = max(10 ** (i - 1), li)
    te = min(10 ** i - 1, ri)

    ## i * 個数 * (最初と最後の値の平均)
    t += i * (te - ts + 1) * (ts + te) // 2
    t %= MOD
print(t)