class Solution:
# 136. Single Number
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a frequency dictionary to count occurrences; return the number with frequency 1.
    def singleNumber(self, nums: list[int]) -> int:
        freqs = {}
        for i in nums:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1

        for key, values in freqs.items():
            if values == 1:
                return key
        