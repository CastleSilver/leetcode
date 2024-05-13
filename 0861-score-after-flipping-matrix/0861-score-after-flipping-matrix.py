class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        # 첫 열을 탐색해서 0인 행은 뒤집어준다.
        for i in range(len(grid)):
            if grid[i][0] == 0:
                newRow = []
                for j in range(len(grid[0])):
                    newRow.append(1-grid[i][j])
                grid[i] = newRow
    
        # 그 다음 열부터는 세로열만 탐색해서 과반수 이상이 0인 경우 열을 뒤집어 준다.
        for i in range(1, len(grid[0])):
            zeroCnt = 0
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    zeroCnt += 1
            if zeroCnt > len(grid)/2:
                for j in range(len(grid)):
                    grid[j][i] = 1-grid[j][i]
        
        # 행을 탐색하면서 합을 계산
        ans = 0
        for i in range(len(grid)):
            ans += int("".join(map(str, grid[i])), 2)
        return ans