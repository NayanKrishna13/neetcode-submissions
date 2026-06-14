class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i]=True
        #pal=set()
        for i in range(2,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if (s[j]==s[k] and (dp[j+1][k-1] or i==2)):
                    #pal.add((j,k))
                    dp[j][k]=True
        res=[]
        def palindrome(j,path):
            if j==n:
                res.append(list(path))
                return 
            for i in range(j,n):
                if dp[j][i]:
                    path.append(s[j:i+1])
                    palindrome(i+1,path)
                    path.pop()
        
        palindrome(0,[])
        return res

                


                            
        


