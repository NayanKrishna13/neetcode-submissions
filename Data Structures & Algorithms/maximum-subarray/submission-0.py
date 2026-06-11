class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        best=nums[0]
        for x in nums:
            curr=max(x,curr+x)
            best=max(best,curr)
        return best
        