class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr=[0,0,0]
        for j in range(len(triplets)):
            if (target[0]>=triplets[j][0]) and (target[1]>=triplets[j][1]) and (target[2]>=triplets[j][2]):
                curr=[max(curr[0],triplets[j][0]),max(curr[1],triplets[j][1]),max(curr[2],triplets[j][2])]
        return curr==target


        