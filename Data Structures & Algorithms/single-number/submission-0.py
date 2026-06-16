class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for j in range(len(nums)):
            x=x^nums[j]
        return x


        