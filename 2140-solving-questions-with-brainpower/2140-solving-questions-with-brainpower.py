class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)

        # Initialize the dp array
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            j = i + questions[i][1] + 1
            dp[i] = max(questions[i][0] + dp[min(n, j)], dp[i+1])
        
        return dp[0]