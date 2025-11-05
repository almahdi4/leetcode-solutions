class Solution:
# 23. Merge k Sorted Lists
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Approach: Collect all values from the lists, sort them, and rebuild the linked list.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        if not values:
            return None
        
        values.sort()

        d = ListNode(0)
        current = d
        
        for v in values:
            current.next = ListNode(v)
            current = current.next
        
        return d.next