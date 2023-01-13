


#全て整数で処理しないと誤差が出る問題

a,b,c = map(int,input().split())

tmp = c**b

if tmp > a :
    print("Yes")
else:
    print("No")