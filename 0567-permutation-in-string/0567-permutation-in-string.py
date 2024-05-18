from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        f1 = defaultdict(int)
        f2 = defaultdict(int)

        for el in s1:
            f1[el] += 1
        
        left = 0
        right = 0

        while right < len(s2):
            
            if s2[right] in f1:
                f2[s2[right]] += 1
                if f2[s2[right]] > f1[s2[right]]:
                    # Remove from left till we encounter s2[right]
                    while s2[left] != s2[right]:
                        f2[s2[left]] -= 1
                        left += 1
                    f2[s2[left]] -= 1
                    left += 1
                right += 1
            else:
                left = right + 1
                right += 1
                f2 = defaultdict(int)
                        
            if f1 == f2:
                return True
                        
        return False
