#!/usr/bin/env python3

from queue import PriorityQueue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value  = value

    def __repr__(self):
        return f"({self.weight}, {self.value}$)"

class Node:
    def __init__(self, level, profit, weight):
        self.level  = level
        self.profit = profit
        self.weight = weight

    def __lt__(self, other):
        return other.weight < self.weight

def upper_bound(solution, n, capacity, items):

    if solution.weight >= capacity:
        return 0

    bound  = solution.profit
    j      = solution.level + 1
    weight = solution.weight

    while j < n and weight + items[j].weight <= capacity:
        weight += items[j].weight
        bound  += items[j].value
        j      += 1

    if j < n:
        bound += int((capacity - weight) * items[j].value / items[j].weight)

    return bound

def knapsack(items, capacity, n):

    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    priority_queue = PriorityQueue()
    solution       = Node(level=-1, profit=0, weight=0)
    priority_queue.put(solution)

    max_profit = 0

    while not priority_queue.empty():
        solution = priority_queue.get()

        if solution.level == -1:
            candidate = Node(level=0, profit=0, weight=0)
        elif solution.level == n -1:
            continue
        else:
            candidate = Node(level=solution.level + 1,
                             profit=solution.profit,
                             weight=solution.weight
                         )

        candidate.profit += items[candidate.level].value
        candidate.weight += items[candidate.level].weight

        if candidate.weight <= capacity and candidate.profit > max_profit:
            max_profit = candidate.profit

        candidate_bound = upper_bound(solution=candidate,
                                      n=n,
                                      capacity=capacity,
                                      items=items)

        if candidate_bound > max_profit:
            priority_queue.put(candidate)

        candidate = Node(level=solution.level + 1, profit=solution.profit, weight=solution.weight)
        candidate_bound = upper_bound(solution=candidate,
                                      n=n,
                                      capacity=capacity,
                                      items=items)

        if candidate_bound > max_profit:
            priority_queue.put(candidate)

    return max_profit

if __name__ == '__main__':

    capacity = 10
    items = [
        Item(4, 40),
        Item(7, 42),
        Item(5, 25),
        Item(3, 12)
    ]
    n = len(items)
    expected = 65
    got = knapsack(items, capacity, n)

    print(f"Test case 1:")
    print(f"\titems = {items} and capacity = {capacity}")
    print(f"\tMaximum possible profit =", got)
    print(f"\texpected == got? {expected == got}")

    capacity = 5
    items = [
        Item(2, 12),
        Item(1, 10),
        Item(3, 20),
        Item(2, 15)
    ]
    n = len(items)
    expected = 37
    got = knapsack(items, capacity, n)

    print(f"Test case 2:")
    print(f"\titems = {items} and capacity = {capacity}")
    print(f"\tMaximum possible profit =", got)
    print(f"\texpected == got? {expected == got}")

    capacity = 10
    items = [
        Item(7, 42),
        Item(3, 12),
        Item(4, 40),
        Item(5, 25)
    ]
    n = len(items)
    expected = 65
    got = knapsack(items, capacity, n)

    print(f"Test case 3:")
    print(f"\titems = {items} and capacity = {capacity}")
    print(f"\tMaximum possible profit =", got)
    print(f"\texpected == got? {expected == got}")
