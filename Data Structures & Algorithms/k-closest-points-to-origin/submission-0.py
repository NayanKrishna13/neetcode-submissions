class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math,heapq
        n=len(points)
        heap=[]
        def dist(x,y):
            return math.sqrt(x**2+y**2)
        for j in range(n):
            if len(heap)<k:
                heapq.heappush(heap,[-dist(points[j][0],points[j][1]),points[j]])
            else:
                d=dist(points[j][0],points[j][1])
                if d<-heap[0][0]:
                    heapq.heapreplace(heap,[-d,points[j]])
        l=[]
        for j in range(k):
            l.append(heap[j][1])
        return l



        