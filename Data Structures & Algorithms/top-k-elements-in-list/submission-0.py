class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        n=len(nums)
        for j in range(n):
            if nums[j] in d:
                d[nums[j]][0]+=1
            else:
                d[nums[j]]=[1,nums[j]]
        l=sorted(d.values(),reverse=True)
        ans=[]
        for j in range(k):
            ans.append(l[j][1])
        return ans
        