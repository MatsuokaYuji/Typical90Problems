n = int(input())

s = []

for i in range(n):
    tmp = input()
    s.append(tmp)

user =set()

#和集合の長さが変わっているか確認、重複するなら集合は変わらない
for i in range(n):
    tmp1 = len(user)
    user.add(s[i])
    tmp2 = len(user)
    if tmp1 != tmp2:
        print(i+1)