"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n=len(intervals)
        if n==1:
            return True
        l=[]
        for j in range(len(intervals)):
            l.append([intervals[j].start,intervals[j].end])
        l.sort()
        for j in range(1,len(l)):
            if l[j][0]<l[j-1][1]:
                return False
        return True
        


