#Program to find the sum of all odd numbers between two given numbers:

start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

sum_of_odds = 0

for num in range(start, stop + 1):
    if num % 2 != 0:
        sum_of_odds += num

print(f"Sum of odd numbers between {start} and {stop}: {sum_of_odds}")
