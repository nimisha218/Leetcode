from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = 0

        d = defaultdict(int)

        left = 0

        for right in range(len(s)):
            
            # Add the character to the freq hash map
            d[s[right]] += 1

            while (right - left + 1 - max(d.values())) > k:
                d[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result