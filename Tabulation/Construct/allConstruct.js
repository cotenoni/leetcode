const allConstruct = (target, wordBank) => {
    const table = Array(target.length + 1)
        .fill()
        .map(() => Array(0));

    table[0] = [[]];

    for (let i = 0; i <= target.length; i++) {
        const current = table[i];

        for (let word of wordBank) {
            if (target.slice(i, i + word.length) === word) {
                const newCombination = current.map(subArray => [ ...subArray, word ]);
                table[i + word.length].push(...newCombination);
            }
        }
    }

    return table[target.length];
};


console.log(allConstruct("", ["cat", "dog", "mouse"])); // [[]]
console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])); // [[ab, cd, ef], [ab, c, def], [abc, def], [abcd, ef]]
console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])); // [ [ 'purp', 'le' ], [ 'p', 'ur', 'p', 'le' ] ]
console.log(allConstruct("skateboard", ["sk", "ateboard", "skate", "board", "ska", "teboard", "boar"])); // [ [ 'sk', 'ateboard' ], [ 'ska', 'teboard' ], [ 'skate', 'board' ] ]
console.log(allConstruct("eeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"])); // []


