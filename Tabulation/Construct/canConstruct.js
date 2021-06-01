const canConstruct = (target, wordBank) => {
    let table = Array(target.length + 1).fill(null);
    table[0] = "";

    for (let i = 0; i <= target.length; i++) {
        const current = table[i];

        if (current !== null) {
            for (let word of wordBank) {
                const concatenation = current + word;

                if (target.startsWith(concatenation)) {
                    table[concatenation.length] = concatenation;
                }
            }
        }
    }

    return table[target.length] === target;
};




console.log(canConstruct("", ["cat", "dog", "mouse"])); // true
console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])); // true
console.log(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])); // false
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"])); // false