class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        profit=0
        for j in range(len(prices)):
            if j==0:
                m=prices[j]
            else:
                if prices[j]<m:
                    m=prices[j]
                else:
                    profit=max(profit,prices[j]-m)
        return profit



        