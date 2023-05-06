def containsDuplicate(self, nums: list[int]) -> bool:
    mySet = set()
    
    for num in nums:
        if num in mySet:
            return True
        
        mySet.add(num)

    return False