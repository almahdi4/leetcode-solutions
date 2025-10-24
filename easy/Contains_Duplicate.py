class Solution:
# 217. Contains Duplicate
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a hash set to detect if a number has already been seen.
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False