class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        remain = k

        for ch in num:
            ch = int(ch)
            while stack and int(stack[-1]) > ch and remain > 0:
                stack.pop()
                remain -= 1
            if not stack and ch == 0:
                continue
            stack.append(str(ch))
        
        while remain > 0 and stack:
            stack.pop()
            remain -= 1

        return "".join(stack) if stack else "0"
        
