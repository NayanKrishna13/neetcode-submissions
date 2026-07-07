class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
            
        # dp[i][1] represents 'buying=True' (looking to buy)
        # dp[i][0] represents 'buying=False' (looking to sell)
        # Pad with 2 extra days to safely handle the i + 2 cooldown transition
        dp = [[0] * 2 for _ in range(n + 2)]
        
        # Iterate backward from the last day to the first day
        for i in range(n - 1, -1, -1):
            # Case 1: We are in a buying state (buying = True -> index 1)
            buy = dp[i + 1][0] - prices[i]
            cooldown_buy = dp[i + 1][1]
            dp[i][1] = max(buy, cooldown_buy)
            
            # Case 2: We are in a selling state (buying = False -> index 0)
            sell = dp[i + 2][1] + prices[i]  # i + 2 captures the mandatory 1-day cooldown
            cooldown_sell = dp[i + 1][0]
            dp[i][0] = max(sell, cooldown_sell)
            
        # The answer matches your initial call: dfs(0, True) -> day 0, buying=True
        return dp[0][1]