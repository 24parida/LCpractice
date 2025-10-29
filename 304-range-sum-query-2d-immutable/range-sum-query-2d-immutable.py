class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        N, M = len(matrix), len(matrix[0])
        self.prefix = [[0] * (M+1) for _ in range(N+1)]

        for i in range(1, N+1):
            for j in range(1, M+1):
                tl = self.prefix[i-1][j-1]
                t = self.prefix[i-1][j]
                l = self.prefix[i][j-1]
                self.prefix[i][j] = (t + l + matrix[i-1][j-1]) - tl

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumBR = self.prefix[row2+1][col2+1]
        sumTL = self.prefix[row1][col1]
        sumBL = self.prefix[row2+1][col1]
        sumTR = self.prefix[row1][col2+1]
        return sumBR - (sumTR + sumBL) + sumTL

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)