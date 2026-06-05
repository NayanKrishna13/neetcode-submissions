class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        l=n-1
        for j in range(n-1,-1,-1):
            if j!=n-1:
                if nums[j]+j>=l:
                    l=j
        if l==0:
            return True
        else:
            return False
            
        

         
