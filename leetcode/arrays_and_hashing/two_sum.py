from typing import List


def twoSum(nums: List[int], target: int) -> list[int] | None:
    # mapping -> value : index
    prevMap = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in prevMap:
            return [prevMap[diff], index]

        prevMap[value] = index

    return
