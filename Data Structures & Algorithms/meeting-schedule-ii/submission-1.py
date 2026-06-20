"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, Interval: List[Interval]) -> int:
        import heapq
        q=[]
        intervals=[]
        for j in range(len(Interval)):
            intervals.append([Interval[j].start,Interval[j].end])
        intervals.sort()
        for j in range(len(Interval)):
            if j==0:
                heapq.heappush(q,intervals[j][1])
            else:
                if intervals[j][0]>=q[0]:
                    heapq.heapreplace(q,intervals[j][1])
                else:
                    heapq.heappush(q,intervals[j][1])
        return len(q)

        