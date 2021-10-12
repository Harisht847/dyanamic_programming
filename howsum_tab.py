def howsum(targetSum, numbers):
    table = [None] * (targetSum+1)
    table[0] = []
    for i in range(len(table)):
        if table[i] != None:
            for j in numbers:
                if i+j< len(table):
                    table[i+j] = table[i] + [j]
    return table[targetSum]
    
print(howsum(7, [5,3,4,7]))
print(howsum(300,[7,14]))
print(howsum(3,[1,2,7]))
print(howsum(7, [2,4]))
print(howsum(8,[2,3,5]))
print(howsum(300,[7,14]))
