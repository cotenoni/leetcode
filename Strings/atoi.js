const myAtoi = (s) => {
    let index = 0;

    while (s[index] === " ") {
        index++;
    }

    let positive = true;
    if (s[index] === "+") {
        index++;
    }
    else if (s[index] === "-") {
        positive = false;
        index++
    }
 
    if (isNaN(s[index]) || s[index] === " ") return 0;
    
    let start = index;
    while (index < s.length && !isNaN(s[index])) {
        index++;
    }
    
    if (index === 0) return 0;

    let value = parseInt(s.substring(start, index));

    if (!positive) value = -value;
    if (value > 0x7FFFFFFF) value = 0x7FFFFFFF
    if (value < -0x7FFFFFFF) value = -0x7FFFFFFF - 1

    return value;
};

console.log(myAtoi("  +  413")) // 0
// console.log(myAtoi("+-12")); // 0
// console.log(myAtoi("42")); // 42
// console.log(myAtoi("   -42")); // -42
// console.log(myAtoi("4193 with words")); // 4193
// console.log(myAtoi("words and 987")); // 0
// console.log(myAtoi("-91283472332")); // -2147483648
// console.log(myAtoi("91283472332")) // 2147483647
// console.log(myAtoi("-2147483647"));
// console.log(myAtoi("-2147483648"));