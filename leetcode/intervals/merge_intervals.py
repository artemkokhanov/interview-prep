from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # O(nlogn) solution where n is the number of intervals we are given because we are first sorting then iterating
    intervals.sort(key=lambda i: i[0])  # sorting by the start values of each interval
    output = [intervals[0]]  # avoiding edge case

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output
