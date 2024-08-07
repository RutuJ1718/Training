#Program to find the number of stones in each pile:

def stone_piles(n):
    return [i for i in range(2, n + 1, 2)] if n % 2 == 0 else [i for i in range(1, n + 1, 2)]

n = 7
stones = stone_piles(n)
print(f"Stones in each pile: {stones}")
