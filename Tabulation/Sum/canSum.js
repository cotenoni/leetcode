const canSum = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(false);
    table[0] = true;

    for (let i = 0; i <= targetSum; i++) {
        const current = table[i];
        if (!current) continue;

        for (let n of numbers) {
            if (i + n <= targetSum) table[i + n] = current;
        }
        
    }

    return table[targetSum];    
};


console.log(canSum(7, [6, 3, 4])); // true
console.log(canSum(5, [1, 2, 3])); // true
console.log(canSum(7, [3, 5])); // false