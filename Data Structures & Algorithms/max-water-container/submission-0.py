class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        ma = 0
        while i < j:
            ma = max(ma, (j - i)*min(heights[j], heights[i]))
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
        return ma
                