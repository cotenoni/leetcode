from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + " -> " + str(self.next)


#https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy_head = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy_head.next

N = ListNode
sol = Solution()
print(sol.mergeTwoLists(None, None))
print(sol.mergeTwoLists(None, N(0)))

l1 = N(1, N(2, N(4)))
l2 = N(1, N(3, N(4)))
print(sol.mergeTwoLists(l1, l2))

