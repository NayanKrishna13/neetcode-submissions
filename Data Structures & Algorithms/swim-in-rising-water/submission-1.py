class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        n=len(grid)
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        distance=defaultdict(int)
        for i in range(n):
            for j in range(n):
                if i==0 and j==0:
                    distance[(i,j)]=grid[i][j]
                else:
                    distance[(i,j)]=float('inf')
        
        q=[(grid[0][0],0,0)]
        while(q):
            dist,x,y=heapq.heappop(q)
            if distance[(x,y)]<dist:
                continue
            for dx,dy in neighbours:
                if (0<=x+dx<n) and (0<=y+dy<n):
                    if max(dist,grid[x+dx][y+dy])<distance[(x+dx,y+dy)]:
                        distance[(x+dx,y+dy)]=max(dist,grid[x+dx][y+dy])
                        heapq.heappush(q,(distance[(x+dx,y+dy)],x+dx,y+dy))
        return distance[(n-1,n-1)]

