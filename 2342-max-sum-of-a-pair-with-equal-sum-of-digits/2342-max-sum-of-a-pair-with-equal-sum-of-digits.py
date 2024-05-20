from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def get_sum(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit
                n = n // 10
            return total
        
        d = defaultdict(list)

        for num in nums:
            cur_sum = get_sum(num)
            d[cur_sum].append(num)
        
        ans = -1

        for key in d:
            temp = d[key]
            if len(temp) > 1:
                temp.sort(reverse=True)
                ans = max(ans, temp[0] + temp[1])
        
        return ans
