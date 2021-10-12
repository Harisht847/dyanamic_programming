

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n] 

print(fib(50))
#print(fib(10))P
#print(fib(50))


#0 1 1 2 3 5 8 13 