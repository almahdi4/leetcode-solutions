class Solution:
# 4. Median of Two Sorted Arrays
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Approach: Merge both sorted arrays into one and compute the median from the merged list.
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = 0
        j = 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
