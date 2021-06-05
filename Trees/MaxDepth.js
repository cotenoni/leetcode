// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
 }
 
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    if (!root) return 0;

    const leftDepth = maxDepth(root.left);
    const rightDepth = maxDepth(root.right);

    return (leftDepth >= rightDepth ? leftDepth : rightDepth) + 1;
};

let root = new TreeNode(
    3,
    new TreeNode(9),
    new TreeNode(
        20, 
        new TreeNode(15),
        new TreeNode(17)
    )
);
console.log(maxDepth(root)); // 3

root = new TreeNode();
console.log(maxDepth(root)); // 1
console.log(maxDepth(null)); // 0

root = new TreeNode(
    1,
    null,
    new TreeNode(2)
);
console.log(maxDepth(root)); // 2