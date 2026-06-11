class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the DP array with a value greater than any possible answer (amount + 1)
        # dp[i] will store the minimum coins needed for amount i
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0
        
        # Iterate through all amounts from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        # If dp[amount] is still infinity, it means the amount cannot be formed
        return dp[amount] if dp[amount] != float('inf') else -1