class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(row, cols, d, antiD):

            if row == n:
                ans[0] += 1
                return
            
            for col in range(n):

                cd = row + col
                cantiD = row - col

                if cd not in d and cantiD not in antiD and col not in cols:
                    d.add(cd)
                    antiD.add(cantiD)
                    cols.add(col)
                    backtrack(row + 1, cols, d, antiD)
                    d.remove(cd)
                    antiD.remove(cantiD)
                    cols.remove(col)
        
        ans = [0]
        backtrack(0, set(), set(), set())
        return ans[0]



                
                
