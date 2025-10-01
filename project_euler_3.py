def largest_prime_factor(n):
    largest_factor = 1
    if n % 2 == 0:
        largest_factor = 2
        while n % 2 == 0:
            n //= 2
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            largest_factor = factor
            while n % factor == 0:
                n //= factor
        factor += 2
    if n > 1:
        largest_factor = n
    return largest_factor

number = 600851475143
result = largest_prime_factor(number)
print(result)
