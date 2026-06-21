class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n=len(heights)
        m=len(heights[0])
        visited=set()
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        ans=[]

        pacific=[[False]*m for _ in range(n)]
        atlantic=[[False]*m for _ in range(n)]

        q1=[(0,0)]
        visited=set()
        visited.add((0,0))
        while(q1):
            x,y=q1.pop()
            pacific[x][y]=True
            for dx,dy in neighbours:
                if (0<=x+dx<n) and (0<=y+dy<m) and ((x+dx,y+dy) not in visited) and (heights[x][y]<=heights[x+dx][y+dy] or (y+dy==0) or (x+dx==0)):
                    q1.append((x+dx,y+dy))
                    visited.add((x+dx,y+dy))
        q1=[(n-1,m-1)]
        visited=set()
        visited.add((n-1,m-1))
        while(q1):
            x,y=q1.pop()
            atlantic[x][y]=True
            for dx,dy in neighbours:
                if (0<=x+dx<n) and (0<=y+dy<m) and ((x+dx,y+dy) not in visited) and (heights[x][y]<=heights[x+dx][y+dy] or (y+dy==m-1) or (x+dx==n-1)):
                    q1.append((x+dx,y+dy))
                    visited.add((x+dx,y+dy))

        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])

        return ans
