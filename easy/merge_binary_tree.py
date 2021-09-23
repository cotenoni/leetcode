# Definition for a binary tree node.
from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        value = str(self.val)
        value += ", " + (str(self.left) if self.left else "null")
        value += ", " + (str(self.right) if self.right else "null")

        return value

#https://leetcode.com/problems/merge-two-binary-trees/   
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        
        queue = collections.deque([(root1, root2)])

        while queue:
            (one, two) = queue.popleft()
    
            if not one or not two:
                continue

            one.val += two.val
            if not one.left:
                one.left = two.left
            else:
                queue.append((one.left, two.left))

            if not one.right:
                one.right = two.right
            else:
                queue.append((one.right, two.right))
            
        return root1


sol = Solution()
N = TreeNode

print(sol.mergeTrees(None, None))
print(sol.mergeTrees(None, N(1, N(2))))
print(sol.mergeTrees(N(1, N(2)), None))

root1 = N(1, N(3, N(5)), N(2))
root2 = N(2, N(1, None, N(4)), N(3, None, N(7)))
print(sol.mergeTrees(root1, root2))

root1 = N(1)
root2 = N(1, N(2))
print(sol.mergeTrees(root1, root2))
