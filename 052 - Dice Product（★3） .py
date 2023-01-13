n= int(input())

A_sum=[]

for i in range(n):
    array = list(map(int, input().split()))
    tmp = 0
    for j in range(len(array)):
        tmp+= array[j]
    A_sum.append(tmp)


ans = 1


for i in range(n):
    ans = ans * A_sum[i] % 1000000007

print(ans)