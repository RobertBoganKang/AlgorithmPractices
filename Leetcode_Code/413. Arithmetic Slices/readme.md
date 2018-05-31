# Solution
Mathematics Problem:

1. Count sub-sequences, such as `[1, 2, 3, 4, 5, 7, 8, 9]`. 
* Get the difference array `[1, 1, 1, 1, 3, 1, 1]`.
* We can get the count array which is `[4, 2]`, where 1 is ignored, since 2 element cannot create sequences.
2. Count the total number.
* Since `[1, 2, 3, 4, 5] -> [1, 1, 1, 1] -> [4]`, we have 7 possible solutions at this case:
```
For 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4], [3, 4, 5];
For 4 arithmetic slices in A: [1, 2, 3, 4], [2, 3, 4, 5]; 
For 5 arithmetic slices in A: [1, 2, 3, 4, 5].
```
This number is `4 - 1 = 3`, then, `3 + 2 + 1 = 7`.

3. The result is calculated.
