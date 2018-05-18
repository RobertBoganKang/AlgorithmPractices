# Solution
* Push element in the max heap, the heap size is k.
* If heap is larger than k, then pop the larger element.
* Then, the heap is maintain the k smaller element, and the top node is the k_th smallest one.
## Analyze
* Time complexity is O(n * log(k))
* Space complexity is O(k)
