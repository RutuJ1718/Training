#Program to check if a string is an anagram of another string:

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if sorted(string1) == sorted(string2):
    print(f"{string1} and {string2} are anagrams")
else:
    print(f"{string1} and {string2} are not anagrams")
