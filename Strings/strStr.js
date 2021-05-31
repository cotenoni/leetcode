// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
const strStr = (haystack, needle) => {
    if (!needle) return 0;
    
    return haystack.indexOf(needle);
};

console.log(strStr("hello", "ll")); // 2
console.log(strStr("aaaaa", "bba")); // -1
console.log(strStr("hello", "")); // 0
console.log(strStr("", "a")); // -1