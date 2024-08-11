from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        res = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            if i == 0:
                stack.append(i)
            else:
                if stack:
                    while stack and temperatures[i] > temperatures[stack[-1]]:
                        t = stack.pop()
                        res[t] = i - t
                stack.append(i)        
        
        return res
