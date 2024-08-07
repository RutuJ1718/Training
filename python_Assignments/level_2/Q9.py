#Program to execute an operation on a list and handle IndexError:

def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

lst = [1, 2, 3, 4, 5]
index = 6
result = get_element_at_index(lst, index)
print(result)
