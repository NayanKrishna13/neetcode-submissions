class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        def backtrack(k,sum,l):
            if sum==target:
                res.append(list(l))
                return
            elif sum>target or k==n:
                return 

            for i in range(k,n):
                if sum+nums[i]>target:
                    break
                if i>k and nums[i]==nums[i-1]:
                    continue
                l.append(nums[i])
                backtrack(i+1,sum+nums[i],l)
                l.pop()
        backtrack(0,0,[])
        return res