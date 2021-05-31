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
    if (!head || !head.next) return head;

    let currentNode = head;
    let nextNode = head.next;

    while (nextNode) {
        const tempNext = nextNode.next;
        const tempCurrent = nextNode;

        nextNode.next = currentNode;
        nextNode = tempNext;
        currentNode = tempCurrent;
    }

    head.next = null;
    return currentNode;
};

let fifth = new ListNode(5);
let fourth = new ListNode(4, fifth);
let third = new ListNode(3, fourth);
let second = new ListNode(2, third);
let head = new ListNode(1, second);
console.log(reverseList(head)); // [5, 4, 3, 2, 1];


// let second = new ListNode(2);
// let head = new ListNode(1, second);
// console.log(reverseList(head)); // [2, 1];


//console.log(reverseList(null)); // [];