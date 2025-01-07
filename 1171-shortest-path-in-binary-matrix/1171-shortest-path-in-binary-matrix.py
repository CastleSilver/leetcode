class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]]
        n = len(grid)
        q = deque()
        q.append(([0, 0], 1))
        grid[0][0] = 1
        while q:
            cur, cnt = q.popleft()
            if cur[0] == n - 1 and cur[1] == n - 1:
                return cnt
            for dir in dirs:
                nx, ny = cur[0] + dir[0], cur[1] + dir[1]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    q.append(([nx, ny], cnt + 1))
                    grid[nx][ny] = 1
        
        return -1