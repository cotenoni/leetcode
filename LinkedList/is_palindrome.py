import collections

#https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current, stack = head, []

        while current:
            stack.append(current.val)
            current = current.next

        current, i = head, 0
        while i <= len(stack) // 2:
            if current.val != stack.pop():
                return False
            i += 1
            current = current.next

        return True


sol = Solution()
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(sol.isPalindrome(head) == True)

head = ListNode(1, ListNode(2))
print(sol.isPalindrome(head) == False)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(sol.isPalindrome(head) == True)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(1))))
print(sol.isPalindrome(head) == False)

head = ListNode(1)
print(sol.isPalindrome(head) == True)
