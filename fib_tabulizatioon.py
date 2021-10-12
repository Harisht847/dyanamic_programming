def fib(n):
    table = [0] * (n+2)
    table[1] = 1
    for i in range(n):
        table[i+1] = table[i]+table[i+1]
        table[i+2] = table[i] + table[i+2]
    return table[n]
()
'''
0 1 1 2 3 5
0 1 1
0   1+1 1+0 0 1 1
i = 2
0 1 1 1+1 1+0
0 1 1 2 2+1 2+0
0 1 1 2 3 5 5+0
0 1 1 2 3 5 8 8+0

'''


print(fib(50))
