from collections import defaultdict

class Solution:
    
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        rows = defaultdict(int)
        cols = defaultdict(int)
        numMap = defaultdict(list)

        num_rows = len(mat)
        num_cols = len(mat[0])

        for row in range(num_rows):
            for col in range(num_cols):
                num = mat[row][col]
                numMap[num] = [row, col]

        for i in range(len(arr)):
            row, col = numMap[arr[i]]
            rows[row] += 1
            cols[col] += 1

            if rows[row] == num_cols or cols[col] == num_rows:
                return i
         
