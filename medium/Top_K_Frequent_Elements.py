class Solution:
# 347. Top K Frequent Elements
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Approach: Use a frequency dictionary to count occurrences, then sort by frequency and return the top k elements.
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        ordered = sorted(count_dict, key=count_dict.get, reverse=True)
        result = []
        for i in range(len(ordered)):
            result.append(ordered[i])
            if len(result) == k:
                return result