index = -1
def linear(number : list,target :int)->int:
    for i in range(len(number)):
        if target == number[i]:
            index = i
    return index
number = [1,2,3,2,5,2]
target = 2
linex = linear(number,target)
if index != -1:
    print("Last Elemen at index :"  , index)
else:
    print("Element not found")