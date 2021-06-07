from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def buildResult(root: TreeNode, level:int):
            if (root is None): return

            if len(self.result) <= level:
                self.result.append([root.val])
            else:
                self.result[level].append(root.val)

            buildResult(root.left, level + 1)
            buildResult(root.right, level + 1)

        self.result = []
        buildResult(root, 0)
        return self.result


solution = Solution()
print(solution.levelOrder(None)) # []

solution = Solution()
root = TreeNode(1)
print(solution.levelOrder(root)) # [[1]]

solution = Solution()
root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)
print(solution.levelOrder(root)) # [[3], [9, 20], [15, 7]]

solution = Solution()
root = TreeNode(
    3,
    TreeNode(
        9,
        TreeNode(1)
    ),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)
print(solution.levelOrder(root)) # [[3], [9, 20], [1, 15, 7]]




