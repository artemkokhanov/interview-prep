# Recursive implementation to calculate the n-th Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# F(0), F(1), F(2), F(3)
# 0,     1,     1,    2
# F(2) = F(1) + F(0)
# F(n) = F(n-1) + F(n-2)
