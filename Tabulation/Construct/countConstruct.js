const countConstruct = (target, wordBank) => {
    let table = Array(target.length + 1).fill(0);
    table[0] = 1;

    for (let i = 0; i <= target.length; i++) {
        const current = table[i];

        if (current) {
            for (let word of wordBank) {
                const concatenation = current + word;

                if (target.startsWith(concatenation)) {
                    table[concatenation.length] += 1;
                }
            }
        }
    }

    return table[target.length];
};


console.log(countConstruct("", ["cat", "dog", "mouse"])); // 1
console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])); // 1
console.log(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])); // false
console.log(countConstruct("skateboard", ["sk", "ateboard", "skate", "board", "ska", "teboard", "boar"])); // 3
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"])); // false