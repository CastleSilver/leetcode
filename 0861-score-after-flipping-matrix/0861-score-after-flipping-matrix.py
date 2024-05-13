class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 첫 열을 탐색해서 0인 행은 뒤집어준다.
        for i in range(m):
            if grid[i][0] == 0:
                newRow = []
                for j in range(n):
                    newRow.append(1-grid[i][j])
                grid[i] = newRow
    
        # 그 다음 열부터는 세로열만 탐색해서 과반수 이상이 0인 경우 열을 뒤집어 준다.
        for i in range(1, n):
            zeroCnt = 0
            for j in range(m):
                if grid[j][i] == 0:
                    zeroCnt += 1
            if zeroCnt > m/2:
                for j in range(m):
                    grid[j][i] = 1-grid[j][i]
        
        # 행을 탐색하면서 합을 계산
        ans = 0
        for i in range(m):
            ans += int("".join(map(str, grid[i])), 2)
        return ans