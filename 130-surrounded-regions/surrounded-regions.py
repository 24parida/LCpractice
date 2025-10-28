class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N, M = len(board), len(board[0])
        self.N, self.M = N, M

        # top row, bottom row
        for x in [0, N-1]:
            for y in range(M):
                self.bfs(x, y, 'T', board)
        
        # left col, right col
        for x in range(N):
            for y in [0, M-1]:
                self.bfs(x, y, 'T', board)
        
        for x in range(N):
            for y in range(M):
                board[x][y] = 'O' if board[x][y] == 'T' else 'X' 
        
        return board
    
    def bfs(self, x, y, ch, board):
        if not (0 <= x < self.N and 0 <= y < self.M):
            return
        if board[x][y] != 'O':
            return
        
        board[x][y] = ch
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for nx, ny in directions:
            new_x, new_y = x + nx, y + ny
            self.bfs(new_x, new_y, ch, board)


        


        