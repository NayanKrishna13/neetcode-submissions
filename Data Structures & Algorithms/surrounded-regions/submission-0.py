class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited=set()
        n=len(board)
        m=len(board[0])
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        def dfs(x,y):
            q=[(x,y)]
            visited.add((x,y))
            while(q):
                x,y=q.pop()
                for dx,dy in neighbours:
                    if (0<=x+dx<n) and (0<=y+dy<m) and board[x+dx][y+dy]=="O" and (x+dx,y+dy) not in visited:
                        q.append((x+dx,y+dy))
                        visited.add((x+dx,y+dy))
            

        for i in range(n):
            for j in range(m):
                if ((i==0 or i==n-1) or (j==0 or j==m-1)) and board[i][j]=="O" and (i,j) not in visited:
                    dfs(i,j)


        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and (i,j) not in visited:
                    board[i][j]="X"
            
                    
        
                
        


        