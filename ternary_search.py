def binary_search(ls,target):
    low = 0
    high = len(ls)-1
    while low <= high:
        mid1 = low+(high-low)//3
        mid2 = high-(high-low)//3
        if ls[mid1] == target:
            return mid1
        elif ls[mid2] == target:
            return mid2
        elif ls[mid1] > target :
            high = mid1 - 1
        elif ls[mid2] < target :
            low = mid2 + 1
        else:
            low=mid1+1
            high=mid2-1
    return -1
ls = [1,2,3,4,5,6,7,8,9]
print(binary_search(ls,8))  