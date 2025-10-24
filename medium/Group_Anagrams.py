class Solution:
# 49. Group Anagrams
# Time Complexity: O(n * k log k), where n = number of words, k = average word length
# Space Complexity: O(n * k)
# Approach: Sort each word to generate a key and group words with identical sorted forms using a hash map.
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in group_anagrams:
                group_anagrams[key].append(word)
            else:
                group_anagrams[key] = [word]
        
        return list(group_anagrams.values())