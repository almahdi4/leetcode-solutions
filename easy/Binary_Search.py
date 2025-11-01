class Solution:
# 704. Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Approach: Classic binary search on a sorted array.
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid - 1
            
            else:
                start = mid + 1
        return - 1
        