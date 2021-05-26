// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
const reverseString = (s) => {
    let j = s.length - 1;

    for (let i = 0; i < s.length / 2; i++) {
            const temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            j--;
    }
    
    return s;
};

console.log(reverseString(["h", "e", "l", "l", "o"])); // ["o", "l", "l", "e", "h"]
console.log(reverseString(["H","a","n","N","a","h"])); // ["h","a","N","n","a","H"]