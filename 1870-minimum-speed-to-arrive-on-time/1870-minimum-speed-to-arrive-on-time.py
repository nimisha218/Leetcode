class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        # Check the base case
        if len(dist) > ceil(hour):
            return -1

        # Define a check method
        def check(k):
            t = 0
            for d in dist:
                t = ceil(t)
                t += d / k
            return t <= hour
        
        # Define the search space
        left = 1
        right = 10 ** 7 # Arbitrary large number (as per the input)

        while left <= right:

            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
            
        return left