class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack = []

        for ch in s:

            stack.append(ch)

            while len(stack) >= len(part) and "".join(stack[len(stack) - len(part):]) == part:
                stack = stack[:len(stack) - len(part)]
        
        
        return "".join(stack)