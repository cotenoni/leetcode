const firstUniqChar = (s) => {
    for (let i = 0; i < s.length; i++) {
        const current = s[i];
        let found = false;

        for (j = 0; j < s.length; j++) {
            if (i !== j) {
                if (s[j] === current) {
                    found = true;
                }
            }
        }

        if (!found) return i;
    }

    return -1;
};

console.log(frstUniqChar("leetcode")); // 0
console.log(frstUniqChar("loveleetcode")); // 2
console.log(frstUniqChar("aabb")); // -1