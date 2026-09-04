def linear(number :list , target : int) -> int:
    for i in range(len(number)):
        if target == number[i]:
            return i
    return -1
number = [1,2,3,4,5]
target = 6
index = linear(number,target)
print(f"{target} is found {index}")