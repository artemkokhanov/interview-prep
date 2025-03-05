def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr

    # the middle index of the array:
    m = (s + e) // 2  # // means floor division, i.e., round down to int

    # sort the left half:
    mergeSort(arr, s, m)

    # sort the right half:
    mergeSort(arr, m + 1, e)

    # merge sorted half's:
    merge(arr, s, m, e)

    return arr


# Merge in-place
def merge(arr, s, m, e):
    # copy the sorted left and right half's to temp arrays:
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0  # index for L
    j = 0  # index for R
    k = s  # index for arr

    # merge the two sorted half's into the original array:
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # one of the half's will have elements remaining:
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
