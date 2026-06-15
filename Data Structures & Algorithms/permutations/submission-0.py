class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        def backtrack(l,s):
            if len(s)==n:
                res.append(list(l))
                return            
            for j in range(n):
                if j not in s:
                    l.append(nums[j])
                    s.add(j)
                    backtrack(l,s)
                    l.pop()
                    s.remove(j)
        backtrack([],set())
        return res



        