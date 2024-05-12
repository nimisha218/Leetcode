class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        seen = set()

        for s in sentence:
            seen.add(s)
        
        return len(seen) == 26
    
    
