const howSum = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = [];

    for (let i = 0; i <= targetSum; i++) {
        const current = table[i];
        
        if (current) {
            for (let n of numbers) {
                if (i + n <= targetSum) {
                    table[i + n] = [ n, ...current ];
                }
            }
        }
    }

    return table[targetSum];    
};


console.log(howSum(7, [2, 3])); // [2, 2, 3]
console.log(howSum(5, [1, 2, 3])); // [1, 1, 1, 1, 1]
console.log(howSum(7, [3, 5])); // null
console.log(howSum(8, [2, 3, 5])); // [2, 2, 2, 2]
console.log(howSum(300, [7, 14])); // null