#Program to count digits and letters in a string:

input_string = input("Enter a string: ")
letters = digits = 0

for char in input_string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

print(f"Alphabets: {letters} & Numbers: {digits}")
