class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        ans=0
        visited=set()
        def dfs(i,j):
            q=[(i,j)]
            visited.add((i,j))
            while(q):
                i,j=q.pop()
                for dx,dy in neighbours:
                    if ((i+dx,j+dy) not in visited) and ((0<=i+dx<n) and (0<=j+dy<m)) and (grid[i+dx][j+dy]=="1"):
                        q.append((i+dx,j+dy))
                        visited.add((i+dx,j+dy))
                    

        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    ans+=1
        return ans
                

        