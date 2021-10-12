def bestsum(targetSum,numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return [] 
    if targetSum < 0:
        return None
    shortestCombination = None
    for num in numbers:
        reminder = targetSum - num 
        reminderResult = bestsum(reminder, numbers, memo)
        if reminderResult != None:
            combination = reminderResult + [num]
            memo[targetSum] = combination
            if (shortestCombination == None) or (len(shortestCombination) > len(combination)):
                shortestCombination = combination

    return shortestCombination


print(bestsum(7, [5,3,4,7]))
'''
print(bestsum(8, [2,3,5]))
print(bestsum(8, [1,4,5]))
print(bestsum(300,[14,7]))

'''