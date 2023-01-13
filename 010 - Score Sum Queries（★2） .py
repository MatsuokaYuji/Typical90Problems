n = int(input())

A= []

for i in range(n):
    s = list(map(int,input().split()))
    A.append(s)

q = int(input())

B = []
for i in range(q):
    t = list(map(int,input().split()))
    B.append(t)
## Q*NだとTLEなので累積和を用いるパターン


tmp1 = 0
tmp2 = 0
sum_score = [[0,0]]
for i in range(n):
    if A[i][0] ==1:
        tmp1 +=A[i][1]
    else:
        tmp2 +=A[i][1]
    sum_score.append([tmp1,tmp2])

for k in range(q):
    count1 = sum_score[B[k][1]][0]-sum_score[B[k][0]-1][0]
    count2 = sum_score[B[k][1]][1]-sum_score[B[k][0]-1][1]
    print(str(count1) + " " + str(count2))

