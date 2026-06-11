class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        ans=0
        for j in range(n):
            dp[j][j]=True
            ans+=1
        
        length=1
        for i in range(2,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if (s[j]==s[k]) and (dp[j+1][k-1] or i==2):
                    ans+=1
                    dp[j][k]=True
        #print(dp)
        return ans
                    
                
        