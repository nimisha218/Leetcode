class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(num):
            ans = ""
            stack = []
            for ch in num:
                if stack:
                    if stack[-1] == ch:
                        stack.append(ch)
                    else:
                        # Count the previous occurences
                        counter = len(stack)
                        n = stack[-1]
                        ans += str(counter)
                        ans += n
                        stack = []
                        stack.append(ch)
                else:
                    stack.append(ch)
            if stack:
                counter = len(stack)
                n = stack[-1]
                ans += str(counter)
                ans += n
            
            return ans

        counter = 1
        res = "1"
        while counter != n:
            res = say(res)
            counter += 1
        return res