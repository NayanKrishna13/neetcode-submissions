class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr,best=-float('inf'),-float('inf')
        for x in nums:
            curr=max(x,curr+x)
            best=max(best,curr)
        return best
        
