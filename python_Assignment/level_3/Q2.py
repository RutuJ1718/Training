#Count the lines in a file demo.txt:

def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)

print(count_lines('demo.txt'))
