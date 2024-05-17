from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = defaultdict(int)

        for el in s:
            d[el] += 1
        
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        s = ""

        for key in d:
            while d[key] != 0:
                s += key
                d[key] -= 1
        
        return s