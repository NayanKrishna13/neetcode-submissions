class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        length=len(word)
        neighbours={(1,0),(-1,0),(0,1),(0,-1)}
        def backtrack(i,j,k):
            if k==length:
                return True
            if (0<=i<n) and (0<=j<m) and (board[i][j]==word[k]):
                temp=board[i][j]
                board[i][j]="."
                res=False
                for (dx,dy) in neighbours:
                    res=res or backtrack(i+dx,j+dy,k+1)
                board[i][j]=temp
                return res
            else:
                return False

        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0):
                        return True
        return False      