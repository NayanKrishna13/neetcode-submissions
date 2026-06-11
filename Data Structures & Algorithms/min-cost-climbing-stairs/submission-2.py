class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n==1:
            return cost[0]
        dp=[0]*n
        for j in range(n):
            dp[j]=cost[j]+min(dp[j-1] if j-1>=0 else 0,dp[j-2] if j-1>=0 else 0)
        print(dp)
        return min(dp[-2],dp[-1])

        