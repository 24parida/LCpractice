class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        i = j = 0

        ## right, down, left, up
        cur = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        visited = set()

        def isValid(x, y):
            return (x,y) not in visited and x < n and x >= 0 and y < m and y >= 0
        

        while isValid(i, j) and len(res) < n * m:
            res.append(matrix[i][j])
            visited.add((i, j))

            dirx, diry = directions[cur]
            nxt_i, nxt_j = i + dirx, j + diry

            if isValid(nxt_i, nxt_j):
                i, j = nxt_i, nxt_j
            else:
                cur = (cur + 1) % 4
                dirx, diry = directions[cur]
                nxt_i, nxt_j = i + dirx, j + diry
                i, j = nxt_i, nxt_j
        
        return res
        