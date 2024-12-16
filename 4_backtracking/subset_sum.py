#!/usr/bin/env python3

def is_valid(current_path, d):
    """
    @param current_sum: the current path being traversed in the tree
    @param d: an integer that represents the desired value for the subset sum
    """
    return sum(current_path) == d

def subset_sum(A, d):
    """
    @param A: list of integers stored in increasing order
    @param d: desired value for the subset sum
    """

    result = []

    if not A:
        return result

    return backtrack(A, d, 0, [], set(), result)

        
def backtrack(A, d, start, current_path, current_sum, paths):
    """
    @param A: list of integers sorted in increasing order
    @param d: an integer that represents the desired value for the subset sum
    @param start: stores the starting node of the tree traversal
    @param path: stores the current path being explored
    @param current_sum: stores the numbers of current path
    @param paths: stores all valid paths
    """

    if is_valid(current_sum, d):
        paths.append(current_path)

    for i in range(start, len(A)):

        if A[i] not in current_sum:
            if sum(current_sum) + A[i] > d: # sum is too large
                break
            elif sum(current_sum) + sum(A[i:]) < d: # sum is too small
                break
            else:
                current_sum.add(A[i])

        backtrack(A, d, i+1, current_path + [A[i]], current_sum, paths)

        current_sum.remove(A[i])

    return paths
 
    
if __name__ == '__main__':

    A = {1,2,5,6,8}
    A = sorted(A)
    d = 9

    solution = subset_sum(A, d)

    print(f"Test case 1")
    print(f"\tA = {A} and d = {d}")
    print(f"\tsolution = {solution}")

    
    A = {3,5,6,7}
    A = sorted(A)
    d = 15

    solution = subset_sum(A, d)

    print(f"Test case 2")
    print(f"\tA = {A} and d = {d}")
    print(f"\tsolution = {solution}")

    A = {}
    A = sorted(A)
    d = 10

    solution = subset_sum(A, d)

    print(f"Test case 3")
    print(f"\tA = {A} and d = {d}")
    print(f"\tsolution = {solution}")
