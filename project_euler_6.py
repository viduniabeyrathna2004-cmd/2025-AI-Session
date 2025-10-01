def sum_square_difference_manual(n):
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i
    sum_of_numbers = 0
    for i in range(1, n + 1):
        sum_of_numbers += i
    square_of_sum = sum_of_numbers * sum_of_numbers

    difference = square_of_sum - sum_of_squares

    return sum_of_squares, square_of_sum, difference
n = 100
sum_sq, sq_sum, diff = sum_square_difference_manual(n)
print(f"Sum of squares: {sum_sq}")
print(f"Square of sum: {sq_sum}")
print(f"Difference: {sq_sum} - {sum_sq} = {diff}")
