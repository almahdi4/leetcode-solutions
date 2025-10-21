class Solution:
# 128. Longest Consecutive Sequence
# Approach: hash set; only start counting from numbers that have no predecessor (x-1 not in set)
# Time Complexity: O(n)
# Space Complexity: O(n)
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        s = set(nums)         
        best = 0

        for x in s:
            if x - 1 not in s:  
                length = 1
                y = x
                while y + 1 in s:
                    y += 1
                    length += 1
                best = max(best, length)
                              
        return best