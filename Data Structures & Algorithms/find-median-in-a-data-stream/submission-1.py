class MedianFinder:
    def __init__(self):
        self.minheap=[]

    def addNum(self, num: int) -> None:
        import bisect
        bisect.insort(self.minheap,num)
        
    def findMedian(self) -> float:
        n=len(self.minheap)
        if n%2==0:
            return (self.minheap[(n+1)//2-1]+self.minheap[(n+1)//2])/2
        else:
            return self.minheap[(n+1)//2-1]
        
        