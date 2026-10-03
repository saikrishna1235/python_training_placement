def merge(arr, res, left, mid, right):
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            res[k] = arr[i]
            k += 1
            i += 1
        else:
            res[k] = arr[j]
            k += 1
            j += 1
    if i > mid:
        while j <= right:
            res[k] = arr[j]
            j += 1
            k += 1
    else:
        while i <= mid:
            res[k] = arr[i]
            i += 1
            k += 1
    for i in range(left, right + 1):
        arr[i] = res[i]

def merge_sort(arr, res, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(arr, res, left, mid)
    merge_sort(arr, res, mid + 1, right)
    merge(arr, res, left, mid, right)
+1
n = int(input("Enter the n value :"))
arr = []
for i in range(n):
    arr.append(int(input()))
res = [0] * n
merge_sort(arr, res, 0, n - 1)
for i in range(n):
    print(arr[i], end=" ")
