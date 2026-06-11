class Solution:
    def climbStairs(self, n: int) -> int:
        f,l=1,2
        if n==1:
            return f
        elif n==2:
            return l
        else:
            for j in range(3,50):
                f,l=l,f+l
                if n==j:
                    return l
        