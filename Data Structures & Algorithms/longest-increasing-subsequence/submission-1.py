class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        l=[]
        for j in nums:
            i=bisect.bisect_left(l,j)
            if i==len(l):
                l.append(j)
            else:
                l[i]=j
        return len(l)

        