#!/usr/bin/env python3

def top_down(items, capacity):
    """
    @param items: list of (weight, value) pairs
    @param capacity: weight supported by the backpack
    """

    n = len(items)
    F = [[0] * (capacity+1) for _ in range(n+1)]

    for i in range(1, n + 1):
        for j in range(1, capacity+1):
            F[i][j] = -1
        
    return MFKnapsack(n, capacity, F, items)

def MFKnapsack(i, j, F, items):
    """
    @param i: integer that indicates the number of the first items being considered
    @param j: nonnegative integer indicating the knapsack capacity
    @param F: memoiziation table
    """

    if i == 0 or j == 0:
        return 0
 
    if j < items[i-1][0]:
        value = MFKnapsack(i - 1, j, F, items)
    else:
        value = max(MFKnapsack(i - 1, j, F, items),
                    items[i-1][1] + MFKnapsack(i - 1, j - items[i-1][0], F, items))

    F[i][j] = value

    return F[i][j]

def bottom_up(items, capacity):
    """
    @param items: list of (weight, value) pairs
    @param capacity: weight supported by the backpack
    """

    n = len(items)
    F = [[0] * (capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if items[i-1][0] <= j:
                with_item = items[i-1][1] + F[i-1][j-items[i-1][0]]
                without_item = F[i-1][j]
                F[i][j] = max(with_item, without_item)
            else:
                F[i][j] = F[i-1][j]

    return F[n][capacity]


if __name__ == '__main__':

    print(f"-------------Bottom-up tests------------------------------------------------")
    # Test case 1
    items = [
        (2, 12),
        (1, 10),
        (3, 20),
        (2, 15),
    ]
    W = 5
    expected = 37
    got = bottom_up(items, W)
    print(f"Test case 1:")
    print(f"\tFour items (weight, value) {items} and capacity = {W}")
    print(f"\texpected = {expected}, got {got}")
    print(f"\texpected == got? {expected == got}")

    # Test case 2
    items = [
        (3, 25),
        (2, 20),
        (1, 15),
        (4, 40),
        (5, 50),
    ]
    W = 6
    expected = 65
    got = bottom_up(items, W)
    print(f"Test case 2:")
    print(f"\tFive items (weight, value) {items} and capacity = {W}")
    print(f"\texpected = {expected}, got {got}")
    print(f"\texpected == got? {expected == got}")

    # Test case 3
    items = [
        (7, 42),
        (3, 12),
        (4, 40),
        (5, 25),
    ]
    W = 10
    expected = 65
    got = bottom_up(items,W)
    print(f"Test case 3:")
    print(f"\tFour items (weight, value) {items} and capacity = {W}")
    print(f"\texpected = {expected}, got {got}")
    print(f"\texpected == got? {expected == got}")

    print(f"---------------------------------------------------------------------------")

    print(f"-------------Top-down tests------------------------------------------------")
    # Test case 1
    items = [
        (2, 12),
        (1, 10),
        (3, 20),
        (2, 15),
    ]
    W = 5
    expected = 37
    got = top_down(items, W)
    print(f"Test case 1:")
    print(f"\tFour items (weight, value) {items} and capacity = {W}")
    print(f"\texpected = {expected}, got {got}")
    print(f"\texpected == got? {expected == got}")

    # Test case 2
    items = [
        (3, 25),
        (2, 20),
        (1, 15),
        (4, 40),
        (5, 50),
    ]
    W = 6
    expected = 65
    got = top_down(items, W)
    print(f"Test case 2:")
    print(f"\tFive items (weight, value) {items} and capacity = {W}")
    print(f"\texpected = {expected}, got {got}")
    print(f"\texpected == got? {expected == got}")

    # Test case 3
    items = [
        (7, 42),
        (3, 12),
        (4, 40),
        (5, 25),
    ]
    W = 10
    expected = 65
    got = top_down(items,W)
    print(f"Test case 3:")
    print(f"\tFour items (weight, value) {items} and capacity = {W}")
    print(f"\texpected = {expected}, got {got}")
    print(f"\texpected == got? {expected == got}")

    print(f"---------------------------------------------------------------------------")
