class Solution:
# 219. Contains Duplicate II
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a hash map to store the last seen index of each number.
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
            