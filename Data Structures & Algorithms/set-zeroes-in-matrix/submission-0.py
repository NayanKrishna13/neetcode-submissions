class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        r=[-1]*n
        c=[-1]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r[i]=0
                    c[j]=0
        for i in range(n):
            for j in range(m):
                if (r[i]==0 or c[j]==0):
                    matrix[i][j]=0
                 


        
        