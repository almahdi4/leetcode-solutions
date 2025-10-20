class Solution:
# 3. Longest Substring Without Repeating Characters
# Time Complexity: O(n)
# Space Complexity: O(k) where k is the alphabet size
# Approach: Sliding window with a set to track current substring characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char = set()       
        longest = 0
        left = 0
        for right, char in enumerate(s):
            while char in seen_char:
                seen_char.remove(s[left])
                left += 1
            seen_char.add(char)
            longest = max(longest, right - left + 1)

        return longest
