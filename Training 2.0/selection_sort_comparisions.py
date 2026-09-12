#find the number of comparisions
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, comparisons
a = [64,25,12,22,11]
sorted_arr, total_comparisons = selection_sort(a)
print(f"Sorted Array: {sorted_arr}")
print(f"Total Comparisons: {total_comparisons}")