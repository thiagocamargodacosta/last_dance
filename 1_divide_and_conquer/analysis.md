Basic operation: comparison

Assuming $n$ is a power of 2:

$T(n) = 2T(n/2) + C_{merge}(n)$ for $n \gt 1$, 
$T(1) = 0$

In the worst case, $C_{merge} = n - 1$

$T(n) = 2T(n/2) + n - 1$

$T(n) = aT(n/b) + f(n)$

$a = 2$

$b = 2$

$f(n) = n - 1$

$f(n) \in \Theta(n)$

$a = b \rightarrow T(n) \in \Theta(n \log n)$
