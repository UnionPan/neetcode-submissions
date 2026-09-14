class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index  
                
            stack.append((start, h))

        for start, h in stack:
            area = max(area, h * (len(heights) - start))
        
        return area
                