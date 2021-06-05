// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
 }

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {

    function validate(root, min, max) {
        if (!root) return true;

        if (root.val <= min || root.val >= max) {
            return false;
        }

        return validate(root.left, min, root.val) && validate(root.right, root.val, max);
    }

    return validate(root.left, Number.MIN_SAFE_INTEGER, root.val) &&
        validate(root.right, root.val, Number.MAX_SAFE_INTEGER);
};

let root = new TreeNode(
    2,
    new TreeNode(1),
    new TreeNode(3)
);
console.log(isValidBST(root)); // true

root = new TreeNode(
    5,
    new TreeNode(1),
    new TreeNode(
        4,
        new TreeNode(3),
        new TreeNode(6)
    )
);
console.log(isValidBST(root)); // false

//[5,4,6,null,null,3,7]
root = new TreeNode(
    5,
    new TreeNode(4),
    new TreeNode(
        6,
        new TreeNode(3),
        new TreeNode(7)
    )
);
console.log(isValidBST(root)); // false

root = new TreeNode(
    1,
    new TreeNode(1)
);
console.log(isValidBST(root)); // false