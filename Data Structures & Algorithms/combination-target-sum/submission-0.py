class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        nums.sort()
        def backtrack(j,k,sum,l):
            if sum==target:
                res.append(list(l))
                return
            elif sum>target:
                return 
            
            for i in range(k,n):
                l.append(nums[i])
                backtrack(j+1,i,sum+nums[i],l)
                l.pop()
        backtrack(0,0,0,[])
        return res
            

        