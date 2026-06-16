class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(s,opn,cls):
            if opn+cls==2*n:
                res.append(s)
                return
            if opn<n:
                backtrack(s+"(",opn+1,cls)
            if cls<opn:
                backtrack(s+")",opn,cls+1)
                
        backtrack("",0,0)
        return res