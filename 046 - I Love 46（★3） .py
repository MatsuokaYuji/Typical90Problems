n = int(input())


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_num = [0 for i in range(46)]
B_num = [0 for i in range(46)]
C_num = [0 for i in range(46)]

for i in range(n):
    tmp_A = A[i]% 46
    tmp_B = B[i]% 46
    tmp_C = C[i]% 46

    A_num[tmp_A] +=1
    B_num[tmp_B] +=1
    C_num[tmp_C] +=1

ans = 0

# あまりの種類は46なので3乗しても計算間に合う

for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k) % 46 == 0:
                ans += A_num[i] * B_num[j] * C_num[k]

print(ans)