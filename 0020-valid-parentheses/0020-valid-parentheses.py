class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        stack = []

        for bracket in s:

            if not stack:
                stack.append(bracket)
                continue
            
            # We know something is in the stack
            if bracket in d:
                stack.append(bracket)
            
            else:
                # It must be a closing bracket
                if stack[-1] not in d:
                    return False
                else:
                    if d[stack[-1]] != bracket:
                        return False
                    else:
                        stack.pop()
        
        if stack:
            return False
        
        return True
            
            
            
