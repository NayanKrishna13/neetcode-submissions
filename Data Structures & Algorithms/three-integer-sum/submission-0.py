class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d={}
        n=len(nums)
        for j in range(n):
            d[nums[j]]=j
        def twosum(k,target):
            l=[]
            visited=set()
            for j in range(k,n):
                if (nums[j] not in visited) and (target-nums[j] in d):
                    if d[target-nums[j]]>j:
                        visited.add(nums[j])
                        l.append([nums[j],target-nums[j]])
            return l
        ans=[]
        vis=set()
        for j in range(n-2):
            if nums[j] not in vis:      
                l=twosum(j+1,-nums[j])
                #print("l,j:",l,j)
                if l:
                    for x in l:
                        x=[nums[j]]+x
                        ans.append(x)
                vis.add(nums[j])
        return ans
