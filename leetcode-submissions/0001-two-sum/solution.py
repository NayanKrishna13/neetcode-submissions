class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=nums.copy()
        n=len(nums)
        nums.sort()
        def binary_search(nums,x):
            f,l=0,n-1
            while(f<=l):
                mid=(f+l)//2
                if nums[mid]==x:
                    return mid
                elif nums[mid]<x:
                    f=mid+1
                else:
                    l=mid-1
            return -1
        first,last=-1,-1
        for j in range(n):
            k=binary_search(nums,target-nums[j])
            if (k!=-1):
                first=nums[j]
                last=nums[k]
                break
        i1,i2=-1,-1
        print(first,last)
        for j in range(n):
            if l1[j]==first:
                i1=j
        for j in range(n):
            if l1[j]==last and i1!=j:
                i2=j
        return [i1,i2]
        
        


                





        """
        :type l: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
