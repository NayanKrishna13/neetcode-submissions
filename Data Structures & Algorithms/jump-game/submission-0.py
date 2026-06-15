class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1:
            return True
        m=0
        for j in range(n):
            if j==0:
                m=max(nums[j]+j,m)
                continue
            if m<j:
                return False
            m=max(m,j+nums[j])

        return True

        