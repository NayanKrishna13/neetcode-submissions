class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        num=0
        intervals.sort()
        for j in range(len(intervals)):
            if j==0:
                curr=intervals[j]
            else:
                if curr[1]>intervals[j][0]:
                    num+=1
                    if intervals[j][1]<=curr[1]:
                        curr=intervals[j]
                else:
                    curr=intervals[j]
        return num




