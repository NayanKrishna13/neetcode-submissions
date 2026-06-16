class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for j in range(n+1):
            ans[j]=bin(j).count("1")
        return ans

        