class Solution:
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