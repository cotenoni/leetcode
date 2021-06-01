const bestSum = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = [];

    for (let i = 0; i <= targetSum; i++) {
        const current = table[i];
        
        if (current) {
            for (let n of numbers) {
                if (!table[i + n] || current.length < table[i + n].length) {
                    table[i + n] = [ n, ...current ];
                }
            }
        }
    }
    
    return table[targetSum];    
};


console.log(bestSum(7, [2, 3])); // [2, 2, 3]
console.log(bestSum(5, [1, 2, 3])); // [2, 3]
console.log(bestSum(7, [3, 5])); // null
console.log(bestSum(8, [2, 3, 5])); // [3, 5]
console.log(bestSum(300, [7, 14])); // null