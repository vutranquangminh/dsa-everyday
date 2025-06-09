class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_max = 0
        right_max = 0
        left = 0
        right = len(height) - 1
        while left < right:
            print(height[right])
            if height[left] < height[right]:
                if left_max < height[left]:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if right_max < height[right]:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water