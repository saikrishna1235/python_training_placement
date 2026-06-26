def ternary_search(ls,target):
    low=0
    high=len(ls)-1
    while low<=high:
        mid1=low+(high+low)//3
        mid2=high-(high+low)//3
        if ls[mid1]==target:
            return mid1
        if ls[mid2]==target:
            return mid2
        if(ls[mid1]<target and ls[mid2]>target):
            low=mid1+1
            high=mid2-1
        elif ls[mid1]>target:
            low=0
            high=mid1-1
        else:
            low=mid2+1
    return -1
ls=[0,1,3,5,7,9,11,13,15]
print(ternary_search(ls,13))