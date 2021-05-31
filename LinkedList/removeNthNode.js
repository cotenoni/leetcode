// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

/**
 * Definition for singly-linked list.
 */
 function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
 const removeNthFromEnd = (head, n) => {    
    if (!head.next) return null;
    
    let currentNode = head;
    let earlierNode = head;
    let index = 0;

    while (currentNode) {
        if (index > n) {
            earlierNode = earlierNode.next;
        }
        index++;

        if (!currentNode.next) {
            break;
        }

        currentNode = currentNode.next;
    }
    // removing head
    if (index === n) return head.next;

    // removing the last node
    if (n === 1) {
        earlierNode.next = null;
    } else {
        // removing any other node
        earlierNode.next = earlierNode.next.next;
    }
    
    return head;
};

// let fifth = new ListNode(5);
// let fourth = new ListNode(4, fifth);
// let third = new ListNode(3, fourth);
// let second = new ListNode(2, third);
// let head = new ListNode(1, second);
// console.log(removeNthFromEnd(head, 2)); // [1, 2, 3, 5];

// let head = new ListNode(1);
// console.log(removeNthFromEnd(head, 1)); // [];

let second = new ListNode(2);
let head = new ListNode(1, second);
console.log(removeNthFromEnd(head, 1)); // [1];

