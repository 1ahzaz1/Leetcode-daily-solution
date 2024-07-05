# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        ptr = head
        indexes = []
        index = 1

        while ptr.next and ptr.next.next:
            if (ptr.val < ptr.next.val > ptr.next.next.val) or (ptr.val > ptr.next.val < ptr.next.next.val):
                indexes.append(index)
            ptr = ptr.next
            index += 1

        if len(indexes) < 2:
            return [-1, -1]

        min_distance = min(b - a for a, b in zip(indexes, indexes[1:]))
        max_distance = indexes[-1] - indexes[0]

        return [min_distance, max_distance]
        