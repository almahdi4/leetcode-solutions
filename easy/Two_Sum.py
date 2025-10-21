class Solution:
# 1. Two Sum
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a hash map to store seen numbers and their indices.
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i