def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
        
        
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result