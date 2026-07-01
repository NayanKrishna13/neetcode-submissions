class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        dist=[float('inf') if (j!=k and j!=0) else 0 for j in range(n+1)]
        child=[[] for _ in range(n+1)]
        for j in range(len(times)):
            child[times[j][0]].append([times[j][1],times[j][2]])
        q=[]
        heapq.heappush(q,[0,k])
        while(q):
            distance,curr=heapq.heappop(q)
            if dist[curr]<distance:
                continue
            for node,d in child[curr]:
                if dist[node]>d+distance:
                    dist[node]=d+distance
                    heapq.heappush(q,[dist[node],node])

        m=max(dist)
        if m==float('inf'):
            return -1
        else:
            return m

