n = int(input())
from itertools import accumulate

A = list(map(int, input().split()))

total = sum(A)

if total % 10 !=0:
    print("No")
else:
    A = A + A
    B = list(accumulate(A))
    sum = total//10
    # print(B)
    # 1 18 1
    # [1, 19, 20, 21, 39, 40]
    l = 0
    for i in range(1,2 * n):
        s = B[i] -B[l]
        if s == sum:
            print("Yes")
            exit()
        elif s > sum:
            l+=1
    print("No")

