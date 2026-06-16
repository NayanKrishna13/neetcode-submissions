class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        def backtrack(j,l):
            if j==n:
                res.append(list(l))
                return 
            l.append(nums[j])
            backtrack(j+1,l)
            l.pop()
            while(j+1<n and nums[j]==nums[j+1]):
                j+=1
            backtrack(j+1,l)
        backtrack(0,[])
        return res

        