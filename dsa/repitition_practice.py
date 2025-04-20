def repetition_practice(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    m = (s + e) // 2

    repetition_practice(arr, s, m)

    repetition_practice(arr, m + 1, e)

    merge(arr, s, m, e)

    return arr


def merge(arr, s, m, e):
    leftSortedArr = arr[s: m + 1]
    rightSortedArr = arr[m + 1: e + 1]

    i = 0  # left sorted arr pointer
    j = 0  # right sorted arr pointer
    k = s  # final location pointer

    while i < len(leftSortedArr) and j < len(rightSortedArr):
        if leftSortedArr[i] <= rightSortedArr[j]:
            arr[k] = leftSortedArr[i]
            i += 1
        else:
            arr[k] = rightSortedArr[j]
            j += 1
        k += 1

    while i < len(leftSortedArr):
        arr[k] = leftSortedArr[i]
        k += 1
    while j < len(rightSortedArr):
        arr[k] = rightSortedArr[j]
        k += 1
