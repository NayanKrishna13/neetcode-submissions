class Solution:
    def countBits(self, n: int) -> List[int]:
        import math
        ans=[0]*(n+1)
        m=0
        for j in range(n+1):
            if j==0:
                ans[j]=j
            elif j==2**(m+1):
                ans[j]=1
                m+=1
            else:
                ans[j]=1+ans[j-2**m]
        return ans


    

        