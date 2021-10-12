
const howsum = (targetSum, numbers, memo={}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    for (let num of numbers){
        const reminder =  targetSum - num;
        const result = howsum(reminder, numbers, memo);
        if (result !== null) {
            memo[targetSum] = [ ...result, num];
            return memo[targetSum]
        }
    }
 memo[targetSum] = null ;  
 return null;
}


console.log(howsum(7,[2,2,3,7]))
console.log(howsum(300, [7,14]))
