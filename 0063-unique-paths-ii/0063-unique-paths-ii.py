class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        obstacleGrid[0][0] = 2 if obstacleGrid[0][0] != 1 else 1
        for j in range(1, m):
            if obstacleGrid[0][j] != 1 and obstacleGrid[0][j-1] != 1 and obstacleGrid[0][j-1] != 0:
                obstacleGrid[0][j] = 2
        
        for i in range(1, n):
            if obstacleGrid[i][0] != 1 and obstacleGrid[i-1][0] != 1 and obstacleGrid[i-1][0] != 0:
                obstacleGrid[i][0] = 2
                
        for i in range(1, n):
            for j in range(1, m):
                if i == 0 or j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                if (obstacleGrid[i][j-1] != 0 and obstacleGrid[i][j-1] != 1) and (obstacleGrid[i-1][j] != 0 and obstacleGrid[i-1][j] != 1):
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j] - 1
                elif obstacleGrid[i][j-1] != 0 and obstacleGrid[i][j-1] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif obstacleGrid[i-1][j] != 0 and obstacleGrid[i-1][j] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
        
        return obstacleGrid[n-1][m-1] - 1 if obstacleGrid[n-1][m-1] != 0 else 0