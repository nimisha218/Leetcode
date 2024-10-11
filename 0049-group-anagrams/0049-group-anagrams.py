from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = defaultdict(list)

        for word in strs:
            c = [0] * 26
            for ch in word:
                c[ord(ch) - ord('a')] += 1
            words[tuple(c)].append(word)
        
        return words.values()

            