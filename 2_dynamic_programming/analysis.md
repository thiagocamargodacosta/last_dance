## Top-down approach

Basic operation: recursive call (`MFKnapsack(i,j,F,items)`)
In the worst case, the F table is accessed two times
Assuming the access takes $O(1)$ time:

$$C(n) = \sum_{i=0}^{n}\sum_{j=1}^{W} = 2n (W+1)$$

$$C(n) = 2nW + 2n \in O(nW)$$

## Bottom-up approach

Basic operation: comparison (`max(with_item, without_item)`)

$$C(n) = \sum_{i=0}^{n}\sum_{j=0}^{W} 1 = (n + 1)\cdot(W + 1) = nW + n + W + 1 \in O(nW)$$
