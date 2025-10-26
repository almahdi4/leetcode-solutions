class Solution:
# 35. Search Insert Position
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Iterate through the array; return the first index where target <= nums[i].
# If not found, return the array's length (insert at the end).
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)