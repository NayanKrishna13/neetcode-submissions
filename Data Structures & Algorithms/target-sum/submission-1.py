class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        def findtarget(i,curr,target):
            if i==len(nums):
                if curr==target:
                    return 1
                else:
                    return 0
            res=0
            if (i,curr) in cache:
                return cache[(i,curr)]
            else:
                res=findtarget(i+1,curr+nums[i],target)+findtarget(i+1,curr-nums[i],target)

            cache[(i,curr)]=res

            return res
            
        
        return findtarget(0,0,target)



