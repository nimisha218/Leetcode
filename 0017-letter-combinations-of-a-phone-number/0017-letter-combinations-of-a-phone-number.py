class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Define the backtrack method
        def backtrack(curr, index):

            # Base case
            if index == len(digits):
                ans.append("".join(curr[:]))
                return

            for letter in phone[int(digits[index])]:
                curr.append(letter)
                backtrack(curr, index + 1)
                curr.pop()
        
        # Populate our digit -> letter hash map
        phone = {
            1: [],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        if digits:
            ans = []
            backtrack([], 0)
            return ans
        return []