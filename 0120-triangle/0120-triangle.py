class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        ans = float('inf')
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] = min(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
                if i==n-1:
                    ans = min(ans, triangle[i][j])
        
        return ans