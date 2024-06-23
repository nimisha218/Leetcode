from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = set()

        ans = 0

        left = 0

        for right in range(len(s)):

            while s[right] in d:
                d.remove(s[left])
                left += 1
            d.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans