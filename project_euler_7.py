def is_prime_manual(n):
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
def find_nth_prime_manual(n):
    if n == 1:
        return 2
    count = 1
    current = 1
    while count < n:
        current += 2
        if is_prime_manual(current):
            count += 1
    return current
result = find_nth_prime_manual(10001)
print(f"The 10,001st is: {result}")
