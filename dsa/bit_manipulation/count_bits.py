def countBits(n):
    count = 0
    while n > 0:
        count += 1
        n = n >> 1  # same as n // 2
    return count


# 23 = 10111
print(countBits(23))
