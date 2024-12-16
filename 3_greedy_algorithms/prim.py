#!/usr/bin/env python3

from sys import maxsize

def prim(G):

    V_t = {0}
    E_t = set()

    for i in range(1, len(G)):
        e = find_minimum_weight_edge(G[i], i, V_t)
        v, u = e
        V_t.add(v)
        E_t.add(u)

    return E_t
    
def find_minimum_weight_edge(edges, v, V_t):

    min_weight = maxsize
    vertex = -1
    
    for i in range(0, len(edges)):
        if i in V_t:
            continue
        elif i == v:
            continue
        else:
            if min_weight > edges[i]:
                min_weight = edges[i]
                vertex     = i

    return (vertex, min_weight)
        

if __name__ == '__main__':

    G = [
        [maxsize, 3, maxsize, maxsize, 6, 5],
        [3, maxsize, 1, maxsize, maxsize, 4],
        [maxsize, 1, maxsize, 6, maxsize, 4],
        [maxsize, maxsize, 6, maxsize, 8, 5],
        [6, maxsize, maxsize, 8, maxsize, 2],
        [5, 4, 4, 5, 2, maxsize],
    ]
    expected = [3,1,4,2,5]
    got = list(prim(G))
    print(f"Test case 1:")
    print(f"\tPrim(G) = {list(got)}")
    print(f"\texpected == got? {expected} == {got}? {expected==got}")
