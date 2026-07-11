class Solution:
    def findMin(self, nums: List[int]) -> int:
        f,l=0,len(nums)-1

        while(f<l):
            mid=f+(l-f)//2
            if (nums[mid]>nums[l]):
                f=mid+1
            else:
                l=mid
        return nums[f]
