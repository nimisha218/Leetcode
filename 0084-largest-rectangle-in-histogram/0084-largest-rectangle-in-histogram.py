class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []

        maxArea = 0

        for i in range(len(heights)):

            if not stack:
                stack.append([i, heights[i]])
                continue
            
            if heights[i] >= stack[-1][1]:
                # Add to the stack
                stack.append([i, heights[i]])
            
            else:
                # Pop from the stack
                while stack and heights[i] < stack[-1][1]:
                    index, height = stack.pop()
                    # Compute potential area
                    maxArea = max(maxArea, (i - index) * height)
                # Add to the stack
                stack.append([index, heights[i]])
        
        i = len(heights)
        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, (i - index) * height)
        
        return maxArea



