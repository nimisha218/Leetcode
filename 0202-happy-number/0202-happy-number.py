class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSum(num):

            ans = 0

            while num > 0:

                digit = num % 10
                ans += (digit ** 2)
                num = num // 10

            return ans
        
        seen = set()
        
        while True:

            curr = getSum(n)
            
            if curr in seen:
                return False
            
            if curr == 1:
                return True
            
            seen.add(curr)

            n = curr
        

