#Program to calculate the sum of digits of a given number until the sum becomes a single-digit number:

num = int(input("Enter a number: "))

def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

while num >= 10:
    num = sum_of_digits(num)

print(f"Final Output: {num}")
