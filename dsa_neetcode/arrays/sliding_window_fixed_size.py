# O(n)
def sliding_window(nums, k):
    window = set()  # Cur window of size <= k
    L = 0
    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False
