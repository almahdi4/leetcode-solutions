class Solution:
# 70. Climbing Stairs
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Dynamic programming (each step depends on the sum of the previous two).
    def climbStairs(self, n: int) -> int:
        steps = {}
        steps[1] = 1
        steps[2] = 2

        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[n]
        