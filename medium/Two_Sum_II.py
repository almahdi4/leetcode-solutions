class Solution:
# 167. Two Sum II - Input Array Is Sorted
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Two-pointer technique; move pointers inward based on sum comparison.
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum == target:
                return [start + 1, end + 1]
            elif curr_sum < target:
                start += 1
            else:
                end -= 1
        