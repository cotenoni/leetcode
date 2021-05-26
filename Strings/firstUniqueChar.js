const firstUniqChar = (s) => {    
    let dict = {};

    for (let i = 0; i < s.length; i++) {
        const current = s[i];

        if (current in dict) {
            dict[current] += 1;
        } else {
            dict[current] = 1;
        }
    }

    for (let i = 0; i < s.length; i++) {
        const current = s[i];

        if (dict[current] === 1) {
            return i;
        }
    }
    return -1;
};

console.log(firstUniqChar("leetcode")); // 0
console.log(firstUniqChar("loveleetcode")); // 2
console.log(firstUniqChar("aabb")); // -1