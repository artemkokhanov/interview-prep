def two_sum(nums, target):
    prev_map = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in prev_map:
            return [prev_map[diff], index]

        prev_map[value] = index

    return
