class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        characters = set()
        result = 0

        left = 0

        for right in range(len(s)):

            while s[right] in characters:
                characters.remove(s[left])
                left += 1
            
            characters.add(s[right])

            currWindow = right - left + 1

            result = max(result, currWindow)
        
        return result