def howsum1(targetSum, numbers):
    if targetSum == 0:
        return True
    if  targetSum < 0 :
        return False 
    for num in numbers:
        reminder =  targetSum - num 
        result = howsum1(reminder, numbers)
        if result:
            return True
    return False


def howsum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        reminder = targetSum - num 
        result = howsum(reminder, numbers, memo)
        if result != None :
            
            memo[targetSum] = result + [num]
            
            return memo[targetSum]
    memo[targetSum] = None 
    return None
        
    
    

    


print(howsum(7,[5,3,4,7]))
print(howsum(300, [7,14,5]))
'''
print(howsum(6, [1,2,3,4,5]))
'''

