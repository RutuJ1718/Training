#Program to reverse the order of words in a given sentence:

input_sentence = "Hello, World! Welcome to Python programming."
reversed_sentence = ' '.join(input_sentence.split()[::-1])
print(f"Output after reverse: {reversed_sentence}")
