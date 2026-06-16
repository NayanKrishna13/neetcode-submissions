class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(s,opn,cls):
            if opn+cls==2*n:
                res.append(''.join(s))
                return
            if opn<n:
                s.append("(")
                backtrack(s,opn+1,cls)
                s.pop()
            if cls<opn:
                s.append(")")
                backtrack(s,opn,cls+1)
                s.pop()
        backtrack([],0,0)
        return res

        