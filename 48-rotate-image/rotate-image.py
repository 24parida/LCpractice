class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r

                tempTopLeft = matrix[top][l + i]

                # top left <- bottom left
                matrix[top][l+i] = matrix[bottom - i][l]

                # bottom left <- bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # bottom right <- top right
                matrix[bottom][r-i] = matrix[top+i][r]

                # top right <- top left
                matrix[top+i][r] = tempTopLeft 
            l, r = l + 1, r-1
        return matrix