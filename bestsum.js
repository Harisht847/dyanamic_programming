const bestsum = (targetsum, numbers) => {
    if (targetsum === 0) return [];
    if (targetsum < 0 ) return null;
    let shortestCombination = null;
    for (let num of numbers) {
        const remainder = targetsum -  num 
        const reminderCombination = bestsum(remainder, numbers)
        if (reminderCombination !== null ) {
            const combination = [...reminderCombination, num];
            if (shortestCombination === null || combination.length < shortestCombination.length)
            {
                shortestCombination = combination;
            }

        }
    }
    return shortestCombination
}


console.log(bestsum(7, [5,3,4,7]))
console.log(bestsum(8, [2,3,5]))
console.log(bestsum(8, [1,4,5]))

