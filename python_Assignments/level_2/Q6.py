#Program to check if a number is a power of two using recursion:

def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    return n % 2 == 0 and is_power_of_two(n // 2)

num = int(input("Enter a number: "))
print(f"Is {num} a power of two? {is_power_of_two(num)}")
