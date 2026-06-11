class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        i=n
        k=-1
        c=0
        for j in range(n):
            if nums[j]<0:
                i=j
                if c==0:
                    k=j
                c+=1
        pro=1
        best=nums[0]
        j=0
        while(j<n):
            best=max(best,pro*nums[j])
            if nums[j]<0 and j==i and c%2!=0:
                pro=1
            elif nums[j]==0:
                pro=1
            else:
                pro*=nums[j]
            j+=1
            #print("pro,best:",pro,best)
        if c%2!=0 and k!=i:
            p=1
            best1=nums[0]
            j=n-1
            while(j>=0):
                best1=max(best1,p*nums[j])
                if nums[j]<0 and j==k:
                    p=1
                elif nums[j]==0:
                    p=1
                else:
                    p*=nums[j]
                j-=1
            return max(best1,best)
        return best






        