from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_value_to_index = {data: i for i, data in enumerate(inorder)}
        
        def helper(preorder_start_idx, preorder_end_idx, inorder_start_idx, inorder_end_idx):
            if preorder_end_idx < preorder_start_idx or inorder_end_idx < inorder_start_idx:
                return None

            root_idx_in_inorder = inorder_value_to_index[preorder[preorder_start_idx]]
            left_subtree_nodes_count = root_idx_in_inorder - inorder_start_idx

            return TreeNode(
                inorder[root_idx_in_inorder],
                helper(preorder_start_idx + 1, preorder_start_idx + left_subtree_nodes_count, inorder_start_idx, root_idx_in_inorder - 1),
                helper(preorder_start_idx + left_subtree_nodes_count + 1, preorder_end_idx, root_idx_in_inorder + 1, inorder_end_idx)
            )

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


solution = Solution()
print(solution.buildTree([10,5,1,8,6,15,20,25,30], [1,5,6,8,10,15,20,30,25]))