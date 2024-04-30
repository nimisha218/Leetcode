class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        result = []

        # Define a digits list
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Define a backtrack method
        def backtrack(num):

            # We found one of the solutions
            if len(num) == n:
                temp = ""
                for q in num:
                    temp += str(q)
                result.append(int(temp))
                return
            
            for digit in digits:
                digit = int(digit)
                if abs(num[-1] - digit) == k:
                    num.append(digit)
                    backtrack(num)
                    num.pop()

        for i in range(1, len(digits)):
            backtrack([int(digits[i])])
        
        return result



        