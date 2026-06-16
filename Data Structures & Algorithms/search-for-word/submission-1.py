class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        length=len(word)
        neighbours={(-1,0),(1,0),(0,-1),(0,1)}
        s=[]
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    s.append((i,j))
        if len(s)==0:
            return False
        res=False
        def backtrack(x,y,k,s1):
            if k==length:
                return True
            for (dx,dy) in neighbours:
                if ((x+dx,y+dy) not in s1) and (0<=x+dx<n) and (0<=y+dy<m) and board[x+dx][y+dy]==word[k]:
                    #print(s1)
                    s1.add((x+dx,y+dy))
                    #print((x+dx,y+dy))
                    if backtrack(x+dx,y+dy,k+1,s1):
                        return True
                    s1.remove((x+dx,y+dy))
            return False

        for (x,y) in s:
            if backtrack(x,y,1,set([(x,y)])):
                return True
        return False







        