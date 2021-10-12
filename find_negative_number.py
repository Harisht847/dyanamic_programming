'''
Find the negative number count in the sorted array...

'''

arr = [[-3,-2,-1,1],[2,2,3,4],[4,5,7,8]]

def find_count(m,n,arr):
    count = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] < 0:
                count +=1
    return count 




def find_count_optimal(m,n,arr):
    count =  0 
    row = 0
    col = n-1
    while col>=0 and row<n:
        
        if arr[row][col]<0:
            count += col+1
            row= row+1
        else:
            col -= 1
    return count 
print(find_count(3,4,arr))
print(find_count_optimal(3,4,arr))