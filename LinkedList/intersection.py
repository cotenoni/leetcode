

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

#https://leetcode.com/problems/intersection-of-two-linked-lists/
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = {}
        
        current = headA
        while current:
            visited[current] = True
            current = current.next

        current = headB
        while current:
            if current in visited:
                return current

            current = current.next
        
        return None


sol = Solution()
N = ListNode

intersect = N(8)
headA = N(4, N(1, intersect))
headB = N(5, N(6, N(1, intersect)))
intersect.next = N(4, N(5))
print(sol.getIntersectionNode(headA, headB) == intersect)

intersect = N(2)
headA = N(1, N(9, N(1, intersect)))
headB = N(3, intersect)
intersect.next = N(4)
print(sol.getIntersectionNode(headA, headB) == intersect)

headA = N(2, N(6, N(4)))
headB = N(1, N(5))
print(sol.getIntersectionNode(headA, headB) == None)