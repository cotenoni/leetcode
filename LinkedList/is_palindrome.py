import collections

#https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #find middle of the list using fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second part of the list
        previous = None
        while slow:
            temp_next = slow.next
            slow.next = previous
            previous = slow
            slow = temp_next
        slow = previous

        #check if any value are different
        while slow:
            if head.val != slow.val:
                return False

            head = head.next
            slow = slow.next

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
