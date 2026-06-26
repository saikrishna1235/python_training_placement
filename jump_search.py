import math
def jump(t):
    l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,271,28,29,30]
    n=len(l)
    print(n)
    j = int(math.sqrt(n))
    p=0
    while(j<n-1):
        p=j
        j+=j*2
    if j>=n:
        j=n-1
    while p<j:
        if l[p] == t:
            return p
        p+=1
    return -1
print(jump(int(input())))
