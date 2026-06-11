class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if n==1:
            if s[0]!="0":
                return 1
            else:
                return 0
        cache={}
        def dfs(j):
            if j in cache:
                return cache[j]
            if j>=n-1:
                return 1
            res=0
            l,r=int(s[j+1]),int(s[j+1]+s[j+2]) if j<n-2 else 27
            if l>0:
                res+=dfs(j+1)
            else:
                cache[j]=0
                return 0
            if r<=26:
                res+=dfs(j+2)
            cache[j]=res
            #print(l,r,res)
            return res

        return dfs(-1)
            
            

        