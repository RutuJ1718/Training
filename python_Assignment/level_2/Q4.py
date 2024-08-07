#Program to rotate array by D elements to the right:

def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    return arr[-d:] + arr[:-d]

arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = rotate_array(arr, d)
print(f"Array after rotation: {rotated_arr}")
