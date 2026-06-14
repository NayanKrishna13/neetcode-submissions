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
        cache={}
        def palindrome(j):
            if j in cache:
                return cache[j]
            if j==n-1:
                return [[(j,j)]]
            res=[]
            for i in range(j,n):
                if dp[j][i]:
                    #print("(j,i):",(j,i))
                    if i==n-1:
                        res.append([(j,n-1)])
                        continue
                    comb=palindrome(i+1)
                    #print("comb:",comb)
                    for x in comb:
                        if x:
                            #print("x:",x)
                            #print("(j,i):",(j,i))
                            l=[(j,i)]
                            l.extend(x)
                            #print("l:",l)
                            res.append(l)
            cache[j]=res
            return res
        #print(dp)
        r=palindrome(0)
        #print("r:",r)
        for x in r:
            for j in range(len(x)):
                x[j]=s[x[j][0]:x[j][1]+1]
        return r

                


                            
        


