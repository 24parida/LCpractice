class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(x, y, i):
            if i == len(word):
                return True
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                return False
            if (x,y) in visited:
                return False
            if board[x][y] != word[i]:
                return False

            visited.add((x,y))
            for nx, ny in directions:
                new_x = x + nx
                new_y = y + ny
                if dfs(new_x, new_y, i + 1):
                    return True
            visited.remove((x,y))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False

