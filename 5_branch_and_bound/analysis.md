We aim to prove the complexity class by using the properties of the search space tree

The worst case as when we cannot prune the search tree when using the best-first strategy

The effective branch factor (EBF) is $2$ since there are two choices:

- `including_item` or
- `not_including_item`

The depth of the search tree - $d$ - is given by the number of items available e.g.:

`items = {(4,40), (7,42), (5, 25), (3,12)}`
`len(items) = 4`

Any EBF where the branching factor - $b$ - is greater than $1$ makes $b^{d}$ an exponential function of $n$

The complexity in the worst case is $O(2^{n})$

---

References

[1] Branch and bound - Why does it work? [https://rjlipton.com/2012/12/19/branch-and-bound-why-does-it-work/](https://rjlipton.com/2012/12/19/branch-and-bound-why-does-it-work/)
