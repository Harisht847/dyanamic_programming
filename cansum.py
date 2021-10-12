

'''
cansum(5,[2,3,4,5]) == > true
cansum(6,[1,2,0,2]) ==> false



def cansum(target,vals):
    for i in range(len(vals)):
        for j in range(len(vals)-1):
            if vals[i] == target or vals[j]==target:
                return True
            if vals[i] + vals[j+1] == target:
                return True
    return False


def cansum1(target,vals):
    i = 0
    while i <= len(vals):
        if vals[i] > target:
            val = vals[i] - target
        else:
            val = target - vals[i]
        if val in vals:
            return True
        i = i+1
    return False

'''
def cansum(target,numbers, memo={}):
    if target in memo:
        return memo[target]
    if target ==  0:
        return True
    if target < 0:
        return False
    for num in numbers:
        reminder = target - num
        if cansum(reminder,numbers,memo) == True:
            memo[target] = True
            return True

    memo[target] = False
    return False

print(cansum(300,[7,14]))
print(cansum(3,[2,7]))
print(cansum(7, [5,3,4,7]))
print(cansum(7, [2,4]))
print(cansum(8,[2,3,5]))
print(cansum(300,[7,14]))
