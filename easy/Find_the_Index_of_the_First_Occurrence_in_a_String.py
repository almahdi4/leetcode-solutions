class Solution:
# 28. Find the Index of the First Occurrence in a String
# Time Complexity: O(n * m)
# Space Complexity: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(haystack) - 1
        while start <= end:
            if haystack[start: start + len(needle)] == needle:
                return start
            else:
                start += 1
        if needle not in haystack:
            return -1