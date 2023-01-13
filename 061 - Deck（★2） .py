
# dequeを使っていない、遅いけどAC,,,794 ms
# q = int(input())

# A = []

# for i in range(q):
#     t,x = map(int,input().split())
#     if t ==1:
#         A.insert(0,x)
#     if t==2:
#         A.append(x)
#     if t==3:
#         print(A[x-1])

# deque使用ver,,,252 ms	

import collections

q = int(input())

T = []
X = []
for i in range(q):
    t, x = map(int,input().split())
    T.append(t)
    X.append(x)

cards = collections.deque()
for i in range(q):
    if T[i] == 1:
        cards.appendleft(X[i])
    elif T[i] == 2:
        cards.append(X[i])
    else:
        print(cards[X[i]-1])
