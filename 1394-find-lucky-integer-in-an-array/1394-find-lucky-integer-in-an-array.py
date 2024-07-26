from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        d = defaultdict(int)
        result = -1

        for num in arr:
            d[num] += 1
        
        for key in d:
            if d[key] == key and key >= result:
                result = key
        
        return result
        

