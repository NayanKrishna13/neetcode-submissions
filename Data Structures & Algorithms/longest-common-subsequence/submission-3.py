class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        prev=[0]*(n+1)
        num=0
        for i in range(1,m+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if text1[j-1]==text2[i-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr
        #print(dp)
        return prev[-1]