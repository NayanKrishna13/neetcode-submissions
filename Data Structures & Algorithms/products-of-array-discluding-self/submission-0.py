class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        front=[1]*n
        back=[1]*n
        l=[0]*n
        for j in range(n):
            if j==0:
                continue

            front[j]=nums[j-1]*front[j-1]
            back[n-j-1]=nums[n-j]*back[n-j]
        for j in range(n):
            l[j]=front[j]*back[j]
        return l
                



        