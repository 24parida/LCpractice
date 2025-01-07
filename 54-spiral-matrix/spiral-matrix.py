class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        size = len(matrix) * len(matrix[0])
        res = []
        while matrix and len(res) != size:
            if matrix and len(res) != size:
                temp = matrix.pop(0)
                res.extend(temp)
            if matrix and len(res) != size:
                for row in matrix:
                    res.append(row.pop())
            if matrix and len(res) != size:
                temp = matrix.pop()
                temp = temp[::-1]
                res.extend(temp)
            if matrix and len(res) != size:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res