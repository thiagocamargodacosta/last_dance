Basic operation: recursive function call (`backtrack(A, d, i + 1, current_path + [A[i]], current_sum, paths)`)

For each subset size ranging from 1 to n, we perform a recursive call
The `for` loop will run $n!$ times

$$C(n) = \sum_{i=0}^{(n-2)!} 1$$
$$C(n) = (n-2)! + 1$$

$$lim_{n->\infty} \frac{(n-2)! + 1}{n!} = \lim_{n->\infty} (\frac{1}{n^{2}-n} + \frac{1}{n!})$$
$$ = \lim_{n->\infty} \frac{1}{x^{2} - x} - \lim{n->\infty} \frac{1}{n!}$$
$$ = 0 + 0 $$

$$C(n) = (n-2)! + 1 \in O(n!)$$
