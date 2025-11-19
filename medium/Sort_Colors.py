class Solution:
# 75. Sort Colors
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Approach: Bubble sort, repeatedly swap adjacent elements until the list is sorted.
# Note: This works correctly but is not optimal.
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    swapped = True