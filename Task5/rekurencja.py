def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial(n: int) -> int:
    total = 1;
    for i in range(1, n + 1):
        total *= i

    return total

