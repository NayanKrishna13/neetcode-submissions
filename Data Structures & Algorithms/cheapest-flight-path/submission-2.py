class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import deque
        q=[]
        distance=[float('inf') if j!=src else 0 for j in range(n)]
        child=[[] for j in range(n)]
        for j in range(len(flights)):
            child[flights[j][0]].append([flights[j][1],flights[j][2]])

        q=deque()
        q.append((0,0,src))
        #visited=[False]*n
        while(q):
            #print(q)
            #print("distance:",distance)
            depth,curr,port=q.popleft()
            for destination,dist in child[port]:
                if curr+dist<distance[destination]:
                    distance[destination]=curr+dist
                    #print(destination,distance[destination])
                    if depth<k:
                        q.append((depth+1,distance[destination],destination))
                
        if distance[dst]==float('inf'):
            return -1
        else:
            return distance[dst]

