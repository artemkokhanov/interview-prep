from typing import List


# runs in O(n) time where n is the length of the input list
def two_sum(nums: List[int], target: int) -> list[int] | None:
    prev_map = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in prev_map:
            return [prev_map[diff], index]

        prev_map[value] = index

    return
