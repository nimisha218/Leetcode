from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s = s.split(" ")
        
        if len(pattern) != len(s):
            return False

        d = defaultdict(str)
        
        for i in range(len(s)):
            if pattern[i] in d:
                if d[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in d.values():
                    return False
                d[pattern[i]] = s[i]
        
        return True
            