#Program to find common elements between two lists:

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

common_elements = [element for element in l1 if element in l2]
print(f"Common elements: {common_elements}")
