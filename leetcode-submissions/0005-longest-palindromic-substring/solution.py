class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        for j in range(n):
            dp[j][j]=True
        maxlen=1
        f,l=0,0
        for i in range(2,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if s[j]==s[k] and (dp[j+1][k-1] or i==2):
                    dp[j][k]=True
                    if maxlen<k-j+1:
                        maxlen=k-j+1
                        f,l=j,k
           
        return s[f:l+1]

        """
        :type s: str
        :rtype: str
        """
        
