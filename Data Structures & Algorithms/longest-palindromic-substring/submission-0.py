class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        for j in range(n):
            dp[j][j]=True
        length=1
        i1=0
        for i in range(2,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if (s[j]==s[k]) and (dp[j+1][k-1] or i==2):
                    if length<i:
                        length=i
                        i1=j
                    dp[j][k]=True
        return s[i1:i1+length]
        

        
        