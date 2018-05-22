# Solution
## Dynamic Programming
* Create a temp array to store the maximum rob case at that point.
* Rob will consider only two cases, if rob `i` house, we will consider `i - 2` and `i - 3`, since `i - 4` has `i - 2` in between and we can rob more if cound rob this house.
* Dynamic programming function: 
```python
temp[i] = max(temp[i - 2], temp[i - 3]) + nums[i]
```
The outside case I use 0 fill up if goes to negative index.
* The maximum of temp array is the answer.
