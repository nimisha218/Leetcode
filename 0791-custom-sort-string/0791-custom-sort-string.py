from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        

        d = defaultdict(int)
        i = 1

        for letter in order:
            d[letter] = i
            i += 1
        
        ignore = set()
        priority = defaultdict(int)

        for letter in s:
            if letter not in d:
                ignore.add(letter)
            else:
                priority[letter] += 1
        
        result = ""

        for letter in order:
            if letter in priority:
                while priority[letter] != 0:
                    result += letter
                    priority[letter] -= 1
        
        for letter in s:
            if letter in ignore:
                result += letter
        
        return result
            