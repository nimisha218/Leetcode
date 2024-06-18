class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def computePower(n): 
            ans = 1
            while n > 0:
                ans *= 4
                n -= 1
            return ans
        
        def checkIfPower(n):
            for i in range(n):
                if computePower(i) == n:
                    return True
                if computePower(i) > n:
                    return False
        
        if n == 1:
            return True
        if n % 4:
            return False
            
        return checkIfPower(n)
