class Solution(object):
    def dfs(self,i,j,matrix,n,m):
        if self.dp[i][j]!=0:
            return self.dp[i][j]
        
        best=1
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        for f,l in d:
            if (0<=i+f<m and 0<=j+l<n and matrix[i][j]<matrix[i+f][j+l]):
                best=max(best,1+self.dfs(i+f,j+l,matrix,n,m))
        self.dp[i][j]=best
        return best

            

    def longestIncreasingPath(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        self.dp=[[0]*n for _ in range(m)]
        c=0
        for i in range(m):
            for j in range(n):
                c=max(c,self.dfs(i,j,matrix,n,m))
        return c
        
