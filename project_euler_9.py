def find_pythagorean_triplet():
    target_sum = 1000
    for a in range(1, target_sum):
        for b in range(a + 1, target_sum - a):
            c = target_sum - a - b
            if c <= b:  # Ensure a < b < c
                continue
            if a * a + b * b == c * c:
                return a, b, c

    return None, None, None
a, b, c = find_pythagorean_triplet()
if a and b and c:
    product = a * b * c
    print(f"Product: {a} × {b} × {c} = {product}")
else:
    print("No triplet found!")
