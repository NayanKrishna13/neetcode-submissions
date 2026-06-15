class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        visited=[False]*n
        def backtrack(l,s):
            if len(l)==n:
                res.append(list(l))
                return            
            for j in range(n):
                if not visited[j]:
                    l.append(nums[j])
                    visited[j]=True
                    backtrack(l,s)
                    l.pop()
                    visited[j]=False
        backtrack([],visited)
        return res



        