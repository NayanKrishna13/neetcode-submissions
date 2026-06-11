class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        def simple_rob(houses):
            rob1,rob2=0,0
            for x in houses:
                rob1,rob2=rob2,max(rob2,rob1+x)
            return rob2
            
        return max(simple_rob(nums[:-1]), simple_rob(nums[1:]))