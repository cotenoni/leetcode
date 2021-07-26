# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        stack = []
        current = root

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                count += 1
                if count == k:
                    return current.val
                current = current.right
            else:
                break


solution = Solution()
tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(solution.kthSmallest(tree, 1)) #1
print(solution.kthSmallest(tree, 2)) #2
print(solution.kthSmallest(tree, 3)) #3
print(solution.kthSmallest(tree, 4)) #4

tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(solution.kthSmallest(tree, 3)) #3

tree = TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(5))
print(solution.kthSmallest(tree, 1)) #2
