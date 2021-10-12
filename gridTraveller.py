
def gridTraveller(m,n,memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[(m,n)] = gridTraveller(m,n-1) + gridTraveller(m-1,n)
    return memo[(m,n)]


print(gridTraveller(180,180))
print(gridTraveller(3,3))
