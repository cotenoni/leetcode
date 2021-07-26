# Definition for a binary tree node.
from typing import List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
            
        NodeWithLevel = collections.namedtuple("NodeWithLevel", ("node", "level"))
        traversal = []
        q = collections.deque([NodeWithLevel(root, 0)])

        while q:
            current_level = [q.popleft()]

            while q and q[0].level == current_level[0].level:
                current_level.append(q.popleft())
                
            traversal.append([])

            for current_node in current_level:
                if current_node.node.left:
                    q.append(NodeWithLevel(current_node.node.left, current_node.level + 1))

                if current_node.node.right:
                    q.append(NodeWithLevel(current_node.node.right, current_node.level + 1))
               
            if current_level[0].level % 2 != 0:
                current_level.reverse()

            for current_node in current_level:
                traversal[current_node.level].append(current_node.node.val)

        return traversal

solution = Solution()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.zigzagLevelOrder(tree)) #[[3],[20,9],[15,7]]

tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
print(solution.zigzagLevelOrder(tree)) #[[1],[3,2],[4,5]]