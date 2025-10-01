def manual_digit_factorial_sum():
    print("Calculating factorials for digits 0-9:")
    factorial = {}
    factorial[0] = 1
    factorial[1] = 1
    factorial[2] = 2
    factorial[3] = 6
    factorial[4] = 24
    factorial[5] = 120
    factorial[6] = 720
    factorial[7] = 5040
    factorial[8] = 40320
    factorial[9] = 362880
    upper_limit = 2500000
    print(f"Checking numbers from 10 to {upper_limit}")
    curious_numbers = []

    for number in range(10, upper_limit + 1):
        num_str = str(number)
        digit_sum = 0
        for digit_char in num_str:
            digit = int(digit_char)
            digit_sum += factorial[digit]
        if digit_sum == number:
            curious_numbers.append(number)
            calculation = " + ".join([f"{int(d)}!" for d in num_str])
            values = " + ".join([str(factorial[int(d)]) for d in num_str])

    return curious_numbers

print("Searching for numbers equal to sum of factorial of their digits...")
print("(This may take a while as we're checking millions of numbers)")
print()

results = manual_digit_factorial_sum()

if results:
    total = sum(results)
    print(f"Sum: {total}")
else:
    print("No numbers found!")
