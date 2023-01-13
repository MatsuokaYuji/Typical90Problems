import math

a,b,c = map(int,input().split())
#最大公約数
d = math.gcd(a,math.gcd(b,c))

ans = (a+b+c)//d-3

print(ans)