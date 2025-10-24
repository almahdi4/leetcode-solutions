class Solution:
# 242. Valid Anagram
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Approach: Sort both strings and compare. If they match, they are anagrams.
    def isAnagram(self, s: str, t: str) -> bool:
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            return True
        else:
            return False