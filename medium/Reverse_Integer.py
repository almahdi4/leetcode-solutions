# 7. Reverse Integer
# Time Complexity: O(log₁₀(n))
# Space Complexity: O(1)
# Approach: Convert the integer to a string, reverse it, and handle sign and overflow.
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            rev = int(str(x)[::-1])
        else:
            rev = -int(str(x)[1:][::-1])
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
    