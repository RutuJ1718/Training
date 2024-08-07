#Program to check if a given string starts with a given character using Lambda:

input_string = "Hello, World!"
given_char = "H"
starts_with = lambda s, c: s.startswith(c)
print(starts_with(input_string, given_char))
