num = [1,2,3,4,5,2]
target = 2
count = 0
for i in range(len(num)):
    if num[i] == target:
        count+=1
print(count)