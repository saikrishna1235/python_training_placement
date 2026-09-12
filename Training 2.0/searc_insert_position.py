def binary(n: list, s: int) -> int:
    left = 0
    right = len(n) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if n[mid] == s:
            return mid
        elif n[mid] < s:
            left = mid + 1
        else:
            right = mid - 1

    return -1


num = [5, 7, 8, 10, 15]
target = 8

print(binary(num, target))