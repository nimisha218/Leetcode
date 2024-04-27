class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(largest):
            subArray = 0
            total = 0
            for num in nums:
                total += num
                if total > largest:
                    subArray += 1
                    total = num
            return subArray + 1 <= k
        
        left = max(nums)
        right = sum(nums)
        res= right

        while left <= right:
            
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
                res = mid
            
            else:
                left = mid + 1
        
        return res

