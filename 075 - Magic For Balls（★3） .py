
N = int(input())

import math

# math.ceil(math.log2(cnt))


a = math.ceil(N **0.5)
cnt = 0

for i in range(2,a+1):
    while N % i ==0:
        cnt+=1
        N = N //i
if N !=1: 
    cnt+=1
if cnt ==0:
    print(0)
else:
    print(math.ceil(math.log2(cnt)))