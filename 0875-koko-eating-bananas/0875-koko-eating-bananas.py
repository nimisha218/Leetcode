class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas/k)
            return hours <= h
        
        # Define the search space
        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

