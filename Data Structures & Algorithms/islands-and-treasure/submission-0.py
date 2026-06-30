class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        n=len(grid)
        m=len(grid[0])
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        q=deque()
        visited=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j,0))
                    visited.add((i,j))
        
        while(q):
            x,y,curr=q.popleft()
            for dx,dy in neighbours:
                if (0<=x+dx<n) and (0<=y+dy<m) and ((x+dx,y+dy) not in visited):
                    if grid[x+dx][y+dy]==2**31-1:
                        grid[x+dx][y+dy]=1+curr
                        q.append((x+dx,y+dy,1+curr))
                    visited.add((x+dx,y+dy))
        