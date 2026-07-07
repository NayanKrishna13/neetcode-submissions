class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        n=len(nums)
        if s%2!=0:
            return False
        else:
            s//=2
            #num=0
            cache={}
            def check(j,num):
                if j in cache:
                    cache[j]
                if num==s:
                    return True
                if j==n:
                    return False

                res=False
                if check(j+1,num+nums[j]):
                    cache[j]=True
                    res=True
                elif check(j+1,num):
                    cache[j]=False
                    res=True

                return res
        
        return check(0,0)


                 



        