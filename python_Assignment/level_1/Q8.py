#Program to calculate the LCM (Least Common Multiple) of two numbers:

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return a * b // calculate_gcd(a, b)

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

lcm = calculate_lcm(number1, number2)

print(f"LCM of {number1} and {number2} is: {lcm}")
