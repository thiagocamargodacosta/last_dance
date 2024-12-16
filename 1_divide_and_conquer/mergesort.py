#!/usr/bin/env python3

from typing import List

def mergesort(A: List[int]):

    n = len(A)

    if n > 1:
        
        B = []
        for i in range(0, n//2):
            B.append(A[i])
        
        C = []
        for i in range(n//2, n):
            C.append(A[i])

        mergesort(B)
        mergesort(C)

        merge(B,C,A)

def merge(B: List[int], C: List[int], A: List[int]):

    p = len(B)
    q = len(C)

    i, j, k = 0, 0, 0

    while i < p and j < q:

        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1

        k = k + 1

    if i == p:
        A[k:p+q] = C[j:q]
    else:
        A[k:p+q] = B[i:p]


if __name__ == '__main__':

    print(f"Test case 1: Input sorted in decreasing order")
    A = [5,4,3,2,1]

    print(f"A:            {A}")
    print(f"A == sorted(A)? {A == sorted(A)}")
    mergesort(A)
    print(f"mergesort(A): {A}")
    print(f"A == sorted(A)? {A == sorted(A)}")
    print(f"--------------------------------\n")
    
    print(f"Test case 2: Input not sorted and with repeating values")
    A = [2,2,2,2,1]
    print(f"A == sorted(A)? {A == sorted(A)}")
    print(f"A:            {A}")
    mergesort(A)
    print(f"mergesort(A): {A}")
    print(f"A == sorted(A)? {A == sorted(A)}")
    print(f"--------------------------------\n")

    print(f"Test case 3: Input with one element out of place")
    A = [1,2,5,4,3]
    print(f"A == sorted(A)? {A == sorted(A)}")
    print(f"A:            {A}")
    mergesort(A)
    print(f"mergesort(A): {A}")
    print(f"A == sorted(A)? {A == sorted(A)}")
