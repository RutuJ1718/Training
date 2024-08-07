#Program to reverse a number using a while loop:

num = int(input("Enter a number: "))
revnum = 0

while num > 0:
    revnum = revnum * 10 + num % 10
    num //= 10

print(f"Reversed number: {revnum}")
