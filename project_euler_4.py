def is_palindrome(n):
    num_str = str(n)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            return False
    return True
def largest_palindrome_product():
    largest = 0
    factors = (0, 0)
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= largest:
                break
            if is_palindrome(product):
                largest = product
                factors = (i, j)
    return largest, factors
largest_pal, (num1, num2) = largest_palindrome_product()
print(f"Largest palindrome product: {largest_pal}")
