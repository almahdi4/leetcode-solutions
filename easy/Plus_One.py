class Solution:
# 66. Plus One
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Convert list of digits to an integer, add one, and convert back to a list.
    def plusOne(self, digits: list[int]) -> list[int]:
        result = 0
        for i in digits:
            result = result * 10 + i
            result_plus_one = result + 1
        return [int(d) for d in str(result_plus_one)]
