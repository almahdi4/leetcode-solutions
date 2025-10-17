class Solution:
# 20. Valid Parentheses
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Stack
    def isValid(self, s: str) -> bool:
        valid_dict = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for i in s:
            if i in valid_dict.values():
                stack.append(i)
            
            if i in valid_dict:
                if stack and valid_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0