def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s  # pointer for left side

    # partition: elements smaller than pivot on the left side:
    for i in range(s, e):
        if arr[i] < pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1

    # move pivot in-between left and right sides:
    arr[e] = arr[left]
    arr[left] = pivot

    # quick sort left side:
    quickSort(arr, s, left - 1)

    # quick sort right side:
    quickSort(arr, left + 1, e)

    return arr
