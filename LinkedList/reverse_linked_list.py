from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            current.next, previous, current = previous, current, current.next

        return previous

L = ListNode
sol = Solution()
print(sol.reverseList(None) == None)

head = L(1, L(2, L(3, L(4, L(5)))))
print(sol.reverseList(head).val == 5)

head = L(1, L(2))
print(sol.reverseList(head).val == 2)


