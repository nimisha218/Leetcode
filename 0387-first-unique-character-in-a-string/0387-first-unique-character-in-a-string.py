class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # Initialize an empty frequency dictionary
        freq = {}

        # Populate the dictionary with the frequencies
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        
        # Check for the first value which has a frequency 1
        match = ""
        for char in s:
            if freq[char] == 1:
                match = char
                break  

        if len(match):
            for i in range(len(s)):
                if s[i] == match:
                    return i
        
        return -1

        