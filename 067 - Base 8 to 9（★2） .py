


import string


n,k = map(int,input().split())


# 覚える
def trans(n:int,b:int) -> string:
    if n//b:
        return trans(n//b,b) + str(n%b)
    return str(n%b)

num= str(n)

for i in range(k):
    base10 = int(num,8)
    base9 = str(trans(base10,9))
    num = ""
    for j in range(len(base9)):
        if base9[j] == "8":
            num+="5"
        else:
            num+=base9[j]

print(num)