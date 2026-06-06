class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i,j,k=0,0,0
        n=len(s1)
        m=len(s2)
        mn=len(s3)
        cache = {}
        def checkinterleaving(i,j,k):
            if (i, j) in cache:
                return cache[(i, j)]
            if k==mn:
                if i==n and j==m:
                    return True
                else:
                    return False
            
            res = False
            if i<n and s1[i]==s3[k]:
                if checkinterleaving(i+1,j,k+1):
                    res = True
            if not res and j<m and s2[j]==s3[k]:
                if checkinterleaving(i,j+1,k+1):
                    res = True
            cache[(i, j)] = res
            return res
        
        return checkinterleaving(0,0,0)