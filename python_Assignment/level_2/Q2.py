#Function to return a list with unique elements:

def get_unique_elements(lst):
    return list(set(lst))

list1 = [1, 2, 2, 3, 4, 4, 5, 5]
list2 = get_unique_elements(list1)
print(f"Unique elements: {list2}")
