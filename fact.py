def fact(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    memo[n] = n * fact(n-1)
    '''print(n * fact(n-1))'''
    print(memo)
    return memo[n]



print(fact(5))
