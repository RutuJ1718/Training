#Function to count the number of vowels in a given string:

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"Number of vowels: {vowel_count}")
