class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap=[]
        for j in range(len(nums)):
            if len(heap)<k:
                heapq.heappush(heap,nums[j])
                continue
            if nums[j]>heap[0]:
                heapq.heapreplace(heap,nums[j])
        return heap[0]


        