class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        heapq.heapify(nums)
        self.nums=nums
        self.k=k

    def add(self, val: int) -> int:
        #import heapq
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums)
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
            return self.nums[0]
        if val>self.nums[0]:
            heapq.heapreplace(self.nums,val)
        return self.nums[0]


        
        
