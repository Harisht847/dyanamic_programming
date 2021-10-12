def cansum(targetSum, numbers):
    table = [False] * (targetSum+1)
    table[0] = True
    for i in range(len(table)):
        for j in numbers:
            #if table[i] and i+j <len(table):
            table[i+j] = True
    return table[targetSum]



print(cansum(300,[7,14]))
print(cansum(3,[2,7]))
print(cansum(7, [5,3,4,7]))
print(cansum(7, [2,4]))
print(cansum(8,[2,3,5]))
print(cansum(300,[7,14]))
