class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        seen_combinations = set()

        result = []

        # Define the backtrack method
        def backtrack(number, seen_numbers):
            
            # Base Case -> We found one of the solutions
            if len(number) == k:
                num = tuple(sorted(number))
                if num not in seen_combinations and sum(number) == n:
                    seen_combinations.add(num)
                    result.append(number[:])
                return
            
            for digit in digits:
                if digit not in seen_numbers:
                    seen_numbers.add(digit)
                    number.append(digit)
                    backtrack(number, seen_numbers)
                    number.pop()
                    seen_numbers.remove(digit)
        
        backtrack([], set())
        return result
                    

