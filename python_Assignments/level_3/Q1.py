#Read the doc.txt file and return only even length strings:

def even_length_strings(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    even_length_words = []
    for line in lines:
        words = line.split()
        for word in words:
            if len(word) % 2 == 0:
                even_length_words.append(word)
    
    return ' '.join(even_length_words)

print(even_length_strings('doc.txt'))
