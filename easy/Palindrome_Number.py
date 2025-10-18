class Solution:
# 9. Palindrome Number
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Convert to string and compare with its reverse.
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else: 
            return False