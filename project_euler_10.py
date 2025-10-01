def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
def sum_primes_manual(limit):

    if limit < 2:
        return 0
    total = 2
    n = 3
    while n < limit:
        if is_prime(n):
            total += n
        n += 2
    return total
limit = 2000000
result = sum_primes_manual(limit)
print(result)
