from collections import deque

class Solution:
    # 'O'의 지역 중에서 바다(map 밖 공간)과 맞닿아 있는 지역을 제외하고 나머지 지역을 'X'로 바꾸는 문제
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 행이나 열이 1인 지역은 바다랑 맞닿을 수 밖에 없기에 탐색에서 제외
        if len(board) == 1 or len(board[0]) == 1:
            return
        visited = [[0 for col in range(len(board[0]))] for row in range(len(board))]
        # 반복문 돌면서 'O' 탐색(가장자리는 탐색할 필요 없음)
        for y in range(1, len(board)-1):
            for x in range(1, len(board[y])-1):
            
                # 1. 'O'일 경우 연결된 cell 있는지 확인
                if board[y][x] == 'O':
                    # 1-1. 연결된 cell 없으면 'X'로 변경
                    if not self.isConnected(y, x, board):
                        board[y][x] = 'X'
                    # 2. 연결된 cell 중에 가장자리 cell 있는지 확인
                    else:
                        # 2-1. 연결된 모든 cell 구하기
                        self.checkLandLocked(y, x, board, visited)
    
    def isConnected(self, y: int, x: int, board: List[List[str]]) -> bool:
        if board[y-1][x] == 'O' or board[y][x-1] == 'O' or board[y][x+1] == 'O' or board[y+1][x] == 'O':
            return True
        else:
            return False
    
    def checkLandLocked(self, y: int, x: int, board: List[List[str]], visited: List[List[int]]) -> None:
        queue = deque()
        self.addRegion(y, x, queue, board, visited)
        isEdge = False
        for i in range(len(queue)):
            y, x = queue[i]
            if y == 0 or x == 0 or y == len(visited) - 1 or x  == len(visited[0]) - 1:
                isEdge = True
                break
        
        if not isEdge:
            while queue:
                y, x = queue.popleft()
                board[y][x] = 'X'
            
        
    def addRegion(self, y: int, x: int, queue: deque, board: List[List[str]], visited: List[List[int]]) -> None:
        if visited[y][x] == 1:
            return
        visited[y][x] = 1
        queue.append([y, x])
        if y > 0 and board[y-1][x] == 'O':
            self.addRegion(y-1, x, queue, board, visited)
        if x > 0 and board[y][x-1] == 'O':
            self.addRegion(y, x-1, queue, board, visited)
        if y < len(board) - 1 and board[y+1][x] == 'O':
            self.addRegion(y+1, x, queue, board, visited)
        if x < len(board[0]) - 1 and board[y][x+1] == 'O':
            self.addRegion(y, x+1, queue, board, visited)
        
        
        
        