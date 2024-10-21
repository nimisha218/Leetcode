class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0

        left = 0
        c = set()

        for right in range(len(s)):

            while s[right] in c:
                c.remove(s[left])
                left += 1
            
            c.add(s[right])

            result = max(result, right - left + 1)

        return result
