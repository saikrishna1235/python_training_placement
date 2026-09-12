'''
Insertion sort :

Insertion sort is a sorting algorithm that builds the sorted array one element at a time 
It takes one element from the inserted portion and insertion it into correct position in the sorted portion.

1.Start from second element 
2.Store the current element as key 
3.Compare kay with the elements before it
4.If the previous element is greater then key 
    move the previous element one position to the right
5.Continue until the correct position is found
6.Insert key into the position 
7.Repeat until the entire array is sorted
'''


def insertion_sort(qrr):
    n = len(arr)
    for i in range(1 , n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [5,3,8,4,2]
insertion_sort(arr)
print(arr)