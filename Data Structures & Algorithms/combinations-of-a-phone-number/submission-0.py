class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        n=len(digits)
        if n==0:
            return res
        def backtrack(i,s):
            if i==n:
                res.append("".join(s))
                return
            f=3*(int(digits[i]))-4 if (digits[i] in {"8","9"}) else 3*(int(digits[i]))-5
            l=4 if (digits[i] in {"7","9"}) else 3 
            for j in range(f,f+l):
                s.append(chr(96+j))
                backtrack(i+1,s)
                s.pop()
        backtrack(0,[])
        return res
            


        