class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s=0
        total=0
        i=0
        n=len(gas)
        for j in range(n):
            s+=gas[j]-cost[j]
            if total+gas[j]-cost[j]<0:
                total=0
                i=(j+1)
            else:
                total+=gas[j]-cost[j]
        if s<0:
            return -1
        else:
            return i

        