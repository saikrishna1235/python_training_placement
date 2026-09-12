def binary(number: list, target : int)-> int:
    left = 0
    right = len(number) - 1
    while left <= right:
        mid = left + (right - left)//2
        if number[mid] == target:
            return mid
        elif number[mid]<target:
            left = mid + 1
        else:
            right = mid -1
    return -1 
number = [10,20,30,40,50,60,70]
target = 60
result=binary(number , target)
print(result)