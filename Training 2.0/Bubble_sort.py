'''
Bubble sort :

Bubble sort is  simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in wrong order.
After every complete pass, the largest element moves to the end  of the unsorted portion of the array.

1.start from the first element 
2.compare the current element with next element.
3.if current element > next element.
    swap both element 
4.move to the next pair of elements
5.continue until the end of the list
6.After, one pass, the largest element will be places at the end.
7. Repeat the process for the remaininng unsorted elements
8.If no swapping happens during a pass:
    The array is already sorted.
9.Stop when array becomes sorted.

'''


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a 
arr = [8,7,3,2,1]
print(bubble_sort(arr))
