class Solution:
    def myPow(self, x: float, n: int) -> float:

        def compute(x, n):

            if n == 0:
                return 1
            
            if n == 1:
                return x
            
            res = compute(x, n//2)
            
            if n % 2:
                # n is odd
                return res * res * x
            
            else:
                return res * res
        
        if x == 0:
            return 0

        if n < 0:
            return 1 / compute(x, abs(n)) 
        
        else:
            return compute(x, n)
        
                
