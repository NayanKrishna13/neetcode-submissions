class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        import bisect
        l=[]
        for j in range(len(intervals)):
            if intervals[j][0]<=newInterval[0]<=intervals[j][1] and intervals[j][0]<=newInterval[1]<=intervals[j][1]:
                return intervals
            if intervals[j][0]<=newInterval[0]<=intervals[j][1]:
                newInterval[0]=intervals[j][0]
            elif intervals[j][0]<=newInterval[1]<=intervals[j][1]:
                newInterval[1]=intervals[j][1]
            elif intervals[j][1]<newInterval[0] or intervals[j][0]>newInterval[1]:
                l.append(intervals[j])
        bisect.insort(l,newInterval)
        return l





