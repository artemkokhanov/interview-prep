from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # O(nlogn) solution where n is the number of intervals we are given because we are first sorting then iterating
    intervals.sort(key=lambda i: i[0])  # sorting by the start values of each interval
    result = [intervals[0]]  # avoiding edge case

    for start, end in intervals[1:]:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(lastEnd, end)
        else:
            result.append([start, end])
    return result
