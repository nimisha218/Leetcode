class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0

        freq = set()

        left = 0

        for right in range(len(s)):
            
            # Shrink the window
            while s[right] in freq:
                freq.remove(s[left])
                left += 1
            
            freq.add(s[right])

            result = max(result, right - left + 1)

        return result