class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        
        N, M = len(mat), len(mat[0])
        directions = [(-1, 1), (1, -1)] # up right, bottom left
        res = []
        cur_dir = 0
        i, j = 0, 0
        while len(res) != N*M:
            res.append(mat[i][j])

            nx, ny = directions[cur_dir]
            new_i = i + nx
            new_j = j + ny

            if not (0 <= new_i < N and 0 <= new_j < M):
                if cur_dir == 0:
                    if new_j >= M:
                        new_i = i + 1
                        new_j = j
                    else:
                        new_i = i
                        new_j = j + 1
                else:
                    if new_i >= N:
                        new_i = i
                        new_j = j + 1
                    else:
                        new_i = i + 1
                        new_j = j
                cur_dir ^= 1
            
            i, j = new_i, new_j

        return res