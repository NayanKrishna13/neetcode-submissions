class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        if n<m:
            return 0
        num=0
        prev=[0]*(n)
        for i in range(m):
            curr=[0]*n
            for j in range(n):
                if i==0:
                    if s[j]==t[i]:
                        curr[j]=1+curr[j-1]
                    else:
                        curr[j]=curr[j-1]
                else:
                    if s[j]==t[i]:
                        curr[j]=(curr[j-1]+prev[j-1]) if j>0 else 0
                    else:
                        curr[j]=curr[j-1]
            prev=curr
        
        return prev[-1]
                




        print(dp)
        return dp[-1][-1]
        


        