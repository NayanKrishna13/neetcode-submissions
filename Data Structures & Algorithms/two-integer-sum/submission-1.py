class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for j in range(len(nums)):
            if nums[j] not in d:
                d[nums[j]]=[j]
            else:
                d[nums[j]].append(j)
        l=[]
        #print(d)
        for j in range(len(nums)):
            if target-nums[j] in d:
                if 2*nums[j]==target:
                    if len(d[nums[j]])>1:
                        l.append(j)
                        l.append(d[nums[j]][1])
                        #print("here")
                        break
                else:
                    l.append(j)
                    l.append(d[target-nums[j]][0])
                    break
        return l


        