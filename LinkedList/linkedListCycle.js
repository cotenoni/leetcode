// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/

/**
 * Definition for singly-linked list.
 */
 function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
 
/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var hasCycle = function(head) {
    if (!head || !head.next) return false;

    let seen = new Set();
    let currentNode = head;

    while (currentNode) {
        if (seen.has(currentNode)) return true;

        seen.add(currentNode);
        currentNode = currentNode.next;
    }

    return false;
};


console.log(hasCycle(null)); // false

let head = new ListNode(1);
console.log(hasCycle(head)); // false


// let second = new ListNode(2)
// let head = new ListNode(1, second);
// second.next = head;
// console.log(hasCycle(head)); // true

// let fourth = new ListNode(-4);
// let third = new ListNode(0, fourth);
// let second = new ListNode(2, third)
// let head = new ListNode(3, second);
// fourth.next = second;
// console.log(hasCycle(head)); // true

