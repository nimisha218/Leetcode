from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        d = defaultdict(int)
        res = 0
        
        for character in s:
            d[character] += 1
            res = d[character]
            
        for key in d:
            if d[key] != res:
                return False
        
        return True
        
        