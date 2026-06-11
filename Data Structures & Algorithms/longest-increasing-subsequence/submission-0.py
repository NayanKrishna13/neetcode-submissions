class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache={}
        n=len(nums)
        def dfs(i):
            length=1
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    if j in cache:
                        length=max(length,1+cache[j])
                    else:
                        length=max(length,1+dfs(j))
                
            cache[i]=length
            return length
        length=1
        for j in range(n-1):
            length=max(length,dfs(j))
        #print(cache)
        return length