class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Phase 1: Swap every diagonal
        for i in range(ROWS):
            for j in range(i, COLS):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Phase 2: Reverse every row
        for i in range(ROWS):
            left = 0
            right = COLS - 1
            for j in range(COLS):
                if left > right:
                    break
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left = left + 1
                right = right - 1

        
        