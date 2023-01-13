import math


a,b = map(int,input().split())

# ansに最小公倍数を計算
ans = a * b // math.gcd(a,b)

if ans > 10**18:
    print("Large")
else:
    print(ans)
