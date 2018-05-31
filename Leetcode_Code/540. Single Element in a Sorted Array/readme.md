# Solution
Use DFS with binary search algorithm:
* Find partition point, which is `round((end - start + 1) / 4) * 2 + start`, where `end` is the position that larger than the last index of array.
* If left last two element is equal, then the single element is on the right subarray, else it in left.
* Until the final one, if there is only one or two element, the answer should be on the left one.
* Terminate the DFS immediately after finding a result and return this result for a function.
