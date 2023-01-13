# %timeit -r 3 -n 1000 n ** 0.5
# # 1000 loops, best of 3: 136 ns per loop
# %timeit -r 3 -n 1000 pow(n, 0.5)
# # 1000 loops, best of 3: 183 ns per loop
# %timeit -r 3 -n 1000 math.sqrt(n)
# # 1000 loops, best of 3: 70.7 ns per loop

#三角関数の問題、復習しないときつい


import math

t = int(input())

l,x,y = map(int,input().split())

r = l/2

q = int(input())

p = math.pi

for i in range(q):
    e = int(input())
    # 観覧車の回転角度
    angle = 2*p*e/t
    # e分の観覧車の位置
    ye = -r * math.sin(angle)
    ze = r - r * math.cos(angle)
    # 観覧車とXY平面上の高橋直大像との距離
    tmp = x**2 + (y-ye)**2
    dist = math.sqrt(tmp)
    # 俯角 tanのz/dist
    dep = math.atan2(ze, dist)

    # print(dep)
    print(math.degrees(dep))


