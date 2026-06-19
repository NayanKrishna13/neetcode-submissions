class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        res=0
        #visited=set()
        def dfs(i,j):
            ans=0
            q=[(i,j)]
            #visited.add((i,j))
            grid[i][j]=0
            while(q):
                i,j=q.pop()
                ans+=1
                for dx,dy in neighbours:
                    if ((0<=i+dx<n) and (0<=j+dy<m)) and (grid[i+dx][j+dy]==1):
                        q.append((i+dx,j+dy))
                        grid[i+dx][j+dy]=0
                #print("ans:",ans)
            return ans
                    
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    res=max(res,dfs(i,j))
        return res