n,l= map(int,input().split())


dp = [0 for _ in range(n+1)]

dp[0] = 1 

for i in range(n):
    if i+1 < l: dp[i+1] = dp[i]
    else: 
        dp[i+1] = (dp[i] + dp[i-l+1]) % 1000000007
print(dp[n])