class Solution:
# 198. House Robber
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: DP with two rolling variables (prev2, prev1). At each house,
# choose max of robbing this one + prev2 or skipping and keeping prev1.
    def rob(self, nums: list[int]) -> int:
        prev2 = 0      
        prev1 = 0           

        for x in nums:
            take = prev2 + x
            skip = prev1
            prev2, prev1 = prev1, max(skip, take)

        return prev1