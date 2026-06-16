class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        maxind=[0]*n
        for j in range(n):
            maxind[j]=max(maxind[j-1],j+nums[j])
        t=n-1
        m=0
        for j in range(n-1,-1,-1):
            if j!=n-1:
                if j==0:
                    m+=1
                if maxind[j]<t:
                    m+=1
                    t=j+1
        return m
            
                    


        