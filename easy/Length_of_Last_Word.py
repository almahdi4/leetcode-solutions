class Solution:
# 58. Length of Last Word
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Split the string by whitespace and return the length of the last word.
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        last_word = l[-1]
        return len(last_word)