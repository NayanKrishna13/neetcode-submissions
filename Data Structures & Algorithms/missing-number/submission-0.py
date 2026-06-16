class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=len(nums)
        b=0
        for j in range(len(nums)):
            a=a^j
            b=b^nums[j]
        return a^b

        