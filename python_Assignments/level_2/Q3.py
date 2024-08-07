#Program to find pairs of elements whose sum is equal to K:

def count_pairs_with_sum(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1
    return count

arr = [1, 2, 3, 4, 5]
k = 6
pair_count = count_pairs_with_sum(arr, k)
print(f"Pair count: {pair_count}")
