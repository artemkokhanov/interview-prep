from typing import List


# runs is O(n*log(n)) because of the .sort method
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda i: i[0])
    result = [intervals[0]]  # avoiding edge case

    for start, end in intervals[1:]:
        lastEnd = result[-1][1]

        if start <= lastEnd:
            result[-1][1] = max(lastEnd, end)
        else:
            result.append([start, end])
    return result
