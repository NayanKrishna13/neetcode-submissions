class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0,0],[0,0],[0,0]]
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums)
        elif n==3:
            return max(nums)
        else:
            for j in range(n):
                if j==0 or j==1:
                    dp[j][0],dp[j][1]=nums[j],j
                elif j==2:
                    dp[2][0],dp[2][1]=dp[0][0]+nums[j],0
                elif j==n-1:
                    k,m=dp[2]
                    dp[2][0]=max((nums[j]+dp[1][0] if dp[1][1]==1 else dp[1][0]-nums[0]+max(nums[j],nums[0])),
                                nums[j]+dp[0][0] if dp[0][1]==1 else dp[0][0]-nums[0]+max(nums[j],nums[0]))

                    dp[0][0],dp[0][1]=dp[1][0],dp[1][1]
                    dp[1][0],dp[1][1]=k,m       
                else:
                    k,m=dp[2]
                    if dp[0][0]<dp[1][0]:
                        dp[2][0],dp[2][1]=dp[1][0]+nums[j],dp[1][1]
                    elif dp[0][0]>dp[1][0]:
                        dp[2][0],dp[2][1]=dp[0][0]+nums[j],dp[0][1]
                    else:
                        dp[2][0],dp[2][1]=dp[0][0],1

                    dp[0][0],dp[0][1]=dp[1][0],dp[1][1]
                    dp[1][0],dp[1][1]=k,m
                #print(dp)
        return max(dp[-1][0],dp[-2][0])


                


        