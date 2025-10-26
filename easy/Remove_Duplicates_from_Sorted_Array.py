class Solution(object):
# 26. Remove Duplicates from Sorted Array
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Use two pointers to overwrite duplicates in-place as we iterate through the sorted array.
    def removeDuplicates(self, nums):
        seen = set()
        insert_pos = 0

        for i in nums:
            if i not in seen:
                seen.add(i)
                nums[insert_pos] = i
                insert_pos += 1
        return insert_pos
