arr1 = [1,3,4]
arr2 = [2,4,6]

left = 0
right = 0

result = []
while left < len(arr1) and right < len(arr2):
    if arr1[left] <arr2[right]:
        result.append(arr1[left])
        left += 1
    else:
        result.append(arr2[right])
        right += 1
result.extend(arr1[left:])
result.extend(arr2[right:])
print(result)
