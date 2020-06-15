#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) Mathematically n^3/n^2 = n, however stepping it out, the algorithm will run n times. IE
| :---- | :-----|
| n | run |
| 1 | 1 |
| 2 | 2 |
| 8 | 8 |

b) O(n^2) because nested loop.

c) O(1) as n is not called, however if n = bunnies then it would be O(n). It is recursive and reduces by 1 each recursive step.

## Exercise II

Use a binary search tree method, thus it would mimic binary search with O(log n).

Create binary tree using n floors
drop from n/2
if egg breaks, the continue down left side
if egg does not break, then cotinue down right side

return f when egg does not break
