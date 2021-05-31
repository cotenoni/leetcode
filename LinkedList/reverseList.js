// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

 function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const reverseList = (head) => {
    let current = head;
    let previous = null;

    while (current) {
        const tempNext = current.next;
        current.next  = previous;
        previous = current;
        current = tempNext;
    }

    return previous;
};

// let fifth = new ListNode(5);
// let fourth = new ListNode(4, fifth);
// let third = new ListNode(3, fourth);
// let second = new ListNode(2, third);
// let head = new ListNode(1, second);
// console.log(reverseList(head)); // [5, 4, 3, 2, 1];


let second = new ListNode(2);
let head = new ListNode(1, second);
console.log(reverseList(head)); // [2, 1];


console.log(reverseList(null)); // [];