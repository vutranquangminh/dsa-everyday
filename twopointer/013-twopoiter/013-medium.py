class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = []
        left = 0
        right = len(heights) - 1
        while left < right:
            square = min(heights[left], heights[right]) * (right - left)
            water.append(square)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max(water)