from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        queue = deque()

        def add_border_o_to_queue():
            for r in range(rows):
                for c in [0, cols-1]:
                    if board[r][c] == 'O':
                        queue.append((r, c))
            for c in range(cols):
                for r in [0, rows-1]:
                    if board[r][c] == 'O':
                        queue.append((r, c))

        def bfs():
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()
                if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                    board[r][c] = 'E'  # Mark as escape
                    for dr, dc in directions:
                        queue.append((r + dr, c + dc))
        
        # Step 1: Add border 'O's to the queue
        add_border_o_to_queue()
        
        # Step 2: Perform BFS to mark all connected 'O's from the border
        bfs()
        
        # Step 3: Modify the board to replace 'O' with 'X' and 'E' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'

# Example usage:
# board = [
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"]
# ]
# Solution().solve(board)
# print(board)
