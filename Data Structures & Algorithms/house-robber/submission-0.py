class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        for j in range(len(nums)):
            dp[j]=nums[j]+max((dp[j-2] if j-2>=0 else 0),(dp[j-3] if j-3>=0 else 0))
        
        return (max(dp[-1],dp[-2]))



        