#Parse an encoded string and return a dictionary:

def parse_encoded_string(encoded_string):
    parts = encoded_string.split('0')
    parts = [part for part in parts if part]
    first_name = parts[0]
    last_name = parts[1]
    id = parts[2]
    return {"first_name": first_name, "last_name": last_name, "id": id}

encoded_string = "Robert0000James00001234"
print(parse_encoded_string(encoded_string))
