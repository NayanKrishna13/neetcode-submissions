class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        n=len(grid)
        m=len(grid[0])
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        q=deque()
        rot=[0,0]
        count=0
        visited=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    visited.add((i,j))
                elif grid[i][j]==1:
                    count+=1
        while(q):
            x,y,curr=q.popleft()
            for dx,dy in neighbours:
                if (0<=x+dx<n) and (0<=y+dy<m) and ((x+dx,y+dy) not in visited):
                    if grid[x+dx][y+dy]==1:
                        rot[0]=1+curr
                        rot[1]+=1
                        q.append((x+dx,y+dy,1+curr))
                    visited.add((x+dx,y+dy))


        if rot[1]==count:
            return rot[0]
        else:
            return -1

        