class Solution(object):
    from collections import deque
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp=[[0]*n for j in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if (i!=0 or j!=0) and (obstacleGrid[i][j]==0):
                    dp[i][j]=(dp[i-1][j] if (i>0 and obstacleGrid[i-1][j]==0)  else 0)+(dp[i][j-1] if (j>0 and obstacleGrid[i][j-1]==0) else 0)
        #print(dp)
        return dp[-1][-1]


            
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
