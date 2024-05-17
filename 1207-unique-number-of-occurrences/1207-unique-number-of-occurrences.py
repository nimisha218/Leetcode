from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        d = defaultdict(int)

        for num in arr:
            d[num] += 1
    
        unique = set()

        for key in d:
            if d[key] in unique:
                return False
            unique.add(d[key])

        return True