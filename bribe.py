
print(minimumBribes([1,2,3,5,4]))
def minimumBribes(q):
    count = 0
    for i in range(len(q)-1):
        if i+1 != q[i]:
            if i+1 < q[i] and  q[i] > q[i+1]:
                count = count + (q[i] - (i+1))
                if (q[i] - (i+1)) > 2:
                    return "Too chaotic"
            if q[i] < q[i+1]:
                count = count + 1
        return count
@
