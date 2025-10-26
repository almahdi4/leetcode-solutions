class Solution:
# 27. Remove Element
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Approach: Iterate through a shallow copy of the list and remove matching elements using .remove()
    def removeElement(self, nums: list[int], val: int) -> int:
        copy = nums[:]
        for i in copy:
            if i == val:
                nums.remove(i)
        return len(nums)
        