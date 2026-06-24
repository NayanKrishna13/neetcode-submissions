class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        import heapq
        q=list(map(lambda x: -x,stones))
        heapq.heapify(q)
        while(len(q)>1):
            if q[0]==min(q[1],q[2] if len(q)>2 else 0):
                heapq.heappop(q)
                heapq.heappop(q)
            else:
                m1=heapq.heappop(q)
                m2=heapq.heappop(q)
                heapq.heappush(q,m1-m2)
        if len(q)==0:
            return 0
        else:
            return -q[0]



        