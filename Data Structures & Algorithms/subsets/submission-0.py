class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(j,l):
            if j==n:
                res.append(list(l))
                return 
            #backtrack(j+1,l)
            l.append(nums[j])
            backtrack(j+1,l)
            l.pop()
            backtrack(j+1,l)
        backtrack(0,[])
        return res
        


        