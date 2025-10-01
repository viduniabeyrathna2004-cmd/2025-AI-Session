def sum_even_fibonacci(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a

        # Generate next Fibonacci number
        a, b = b, a + b

    return total
result = sum_even_fibonacci(4000000)
print({result})
