#Number of customers that walked away without using a computer:

def count_customers_walk_away(N, S):
    occupied = set()
    walked_away = 0
    customer_in_cafe = set()

    for char in S:
        if char not in customer_in_cafe:
            customer_in_cafe.add(char)
            if len(occupied) < N:
                occupied.add(char)
            else:
                walked_away += 1
        else:
            customer_in_cafe.remove(char)
            if char in occupied:
                occupied.remove(char)
    
    return walked_away

N = 3
S = "GACCBDDBAGEE"
print(count_customers_walk_away(N, S))
