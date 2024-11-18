from collections import defaultdict
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        td = Counter(t)
        sd = defaultdict(int)

        result = ""
        min_length = float('inf')

        have = 0

        need = len(td)

        left = 0

        for right in range(len(s)):
            
            if s[right] in td:
                sd[s[right]] += 1

                if sd[s[right]] == td[s[right]]:
                    have += 1
                
                while have == need:
                    if right - left + 1 < min_length:
                        min_length = right - left + 1
                        result = s[left:right+1]
                    sd[s[left]] -= 1
                    if s[left] in td and sd[s[left]] < td[s[left]]:
                        have -= 1
                    if sd[s[left]] == 0:
                        del sd[s[left]]
                    left += 1
        
        return result

