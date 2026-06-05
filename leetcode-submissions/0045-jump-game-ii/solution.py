class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        l=n-1
        c=1
        l1=[0]*n
        for j in range(n):
            l1[j]=max(l1[j-1],nums[j]+j)

        for j in range(n-2,-1,-1):
            if l1[j]<l:
                l=j+1
                c+=1
        
        return c

            
        
