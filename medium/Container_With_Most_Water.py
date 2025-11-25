class Solution:
# 11. Container With Most Water
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two-pointer, start at both ends, calculate area, and move the pointer at the shorter line inward.

    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_container = 0

        while left < right:
            curr_height = min(height[left], height[right]) 
            curr_container = curr_height * (right - left)
            if curr_container > max_container:
                max_container = curr_container

            elif height[left] < height[right]:
                left += 1
            
            else:
                right -= 1

        return max_container