from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        result = []
        for key in anagrams:
            result.append(anagrams[key])
        
        return result