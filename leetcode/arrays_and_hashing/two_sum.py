from typing import List


def two_sum(nums: List[int], target: int) -> list[int] | None:
    prev_map = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in prev_map:
            return [prev_map[diff], index]

        prev_map[value] = index

    return
