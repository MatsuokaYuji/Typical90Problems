h,w = map(int, input().split())


#例外に気をつけるかつパターンを見つける
ans = 0

if h ==1 or w ==1:
    ans = h*w
else:
    ans = ((h+1)//2) * ((w+1)//2)

print(ans)