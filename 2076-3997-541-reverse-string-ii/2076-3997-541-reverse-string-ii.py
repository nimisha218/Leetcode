class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        s = list(s)
        if k > len(s) - 1:
            return "".join(s[::-1])

        for i in range(0, len(s), 2*k):
            s[i:i+k] = (s[i:i+k])[::-1]
        
        return "".join(s)