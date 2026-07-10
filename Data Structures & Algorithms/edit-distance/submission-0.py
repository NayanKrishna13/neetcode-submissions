class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        cache={}
        def allquietonthewesternfront(i,j):
            if (i,j) in cache:
                return cache[(i,j)]

            if j==m:
                return abs(n-i)
            if i==n:
                return abs(m-j)
            res=0
            if word1[i]==word2[j]:
                res=allquietonthewesternfront(i+1,j+1)
            else:
                res=1+min(allquietonthewesternfront(i+1,j+1),allquietonthewesternfront(i+1,j),allquietonthewesternfront(i,j+1))
            cache[(i,j)]=res
            #print("i,j,res:",i,j,res)
            return res
        return allquietonthewesternfront(0,0)



        
        


