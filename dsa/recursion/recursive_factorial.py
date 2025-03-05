# Recursive implementation of n! (n-factorial) calculation
def factorial(n):
    # Base case: n = 0 or 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)

# 1! = 1
# 2! = 2*1
# 3! = 3*2*1
# n! = n*(n-1)!
