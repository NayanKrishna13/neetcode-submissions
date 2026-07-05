class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        nums=sorted(list(set(nums)))
        n=len(nums)
        c,m=1,1
        for j in range(1,n):
            if nums[j]==nums[j-1]+1:
                c+=1
            else:
                m=max(c,m)
                c=1
        return max(m,c)
    