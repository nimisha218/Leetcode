class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for ch in s:

            if not stack:
                if ch not in d:
                    return False
                else:
                    stack.append(ch)
                    continue
            
            else:
                # There is something in our stack
                if ch not in d:
                    if d[stack[-1]] != ch:
                        return False
                    else:
                        stack.pop()
                else:
                    stack.append(ch)
        
        return len(stack) == 0
            
            

            
        
