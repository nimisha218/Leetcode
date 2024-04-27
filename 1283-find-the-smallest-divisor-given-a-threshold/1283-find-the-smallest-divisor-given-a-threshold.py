class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check(k):

            total = 0
            for num in nums:
                total += ceil(num/k)
            return total <= threshold
        
        # Define the search space
        left = 1
        right = 10 ** 7

        while left <= right:

            mid = (left + right) // 2
            
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left