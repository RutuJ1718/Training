#Run-length encoding of a string:

def run_length_encode(s):
    if not s:
        return ""
    
    encoded_string = ""
    prev_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded_string += f"{prev_char}{count}"
            prev_char = char
            count = 1
    encoded_string += f"{prev_char}{count}"
    
    return encoded_string

input_string = "wwwwaaadebbbbbw"
print(run_length_encode(input_string))
