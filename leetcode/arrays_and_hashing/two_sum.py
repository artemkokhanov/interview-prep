def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in prevMap:
            return [prevMap[diff], index]
        
        prevMap[value] = index
    
    return