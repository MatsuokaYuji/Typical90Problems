



import collections

def bfs(x):
    #頂点xからの距離
    dist = [-1 for i in range(n)]
    #頂点xから最も遠い距離
    max_dist = 0
    #頂点xから最も遠い頂点
    max_point = 0

    que = collections.deque()
    que.append(x)
    dist[x] = 0

    while len(que) != 0:
        p = que.popleft()
        tmp = dist[p] + 1
        for i in  graph[p]:
            if dist[i] != -1:
                continue
            elif tmp > max_dist:
                max_point = i
            que.append(i)
            dist[i] = tmp
            max_dist = max(tmp,max_dist)
    return max_point,max_dist



n = int(input())

graph = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)



# 頂点0から最も遠い頂点point
point,_ = bfs(0)
# 頂点pointから最も遠い距離far
_,far = bfs(point)
# 答えはfar + 1
ans = far + 1

print(ans)