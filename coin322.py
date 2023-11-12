coins = [2,10,20,50]
amount = 110
sum = 0

dp = [amount+1]*(amount + 1)
dp[0]=0
# dp[1]=1
for i in range(1 , amount + 1):
    for j in coins:
        if i - j >= 0:
            dp[i] = min(dp[i], 1 + dp[i - j])

if dp[amount] != amount + 1:
    print(dp[amount])
else:
    print(-1)


