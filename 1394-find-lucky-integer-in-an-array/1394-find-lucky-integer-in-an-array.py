from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        d = defaultdict(int)

        ans = []
        for num in arr:
            d[num] += 1
        
        for key in d:
            if d[key] == key:
                ans.append(key)
        
        if len(ans) > 0:
            return max(ans)
        else:
            return -1