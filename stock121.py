class Solution:
    def maxProfit(self, prices) -> int:
        i,j,max_profit = 0,1,0
        while j<len(prices):
            if prices[i]>=prices[j]:
                i=j
                j+=1
            else:
                buy = prices[i]
                profit = prices[j]-prices[i]
                max_profit = max(max_profit,profit)
                j+=1
                
        return(max_profit)