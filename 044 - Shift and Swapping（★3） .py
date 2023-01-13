



# シフトしてるとTLE
n,q = map(int,input().split())

A = list(map(int, input().split()))


shift = 0
for i in range(q):
    t,x,y = map(int,input().split())
    num_x = (x-1-shift)%n
    num_y = (y-1-shift)%n

    if t == 1:
        tmp = A[num_x]
        A[num_x] = A[num_y]
        A[num_y] = tmp

    elif t == 2:
        shift+=1

    else:
        print(A[num_x])
