# One Line Drawing Game
## Explanation
* Given an initial position
* Use one line to pass all the position
* Only some of the positions are avaiable to pass
## For Example
Given a pathway matrix
```python
[[1, 1, 1, 1, 1, 1],
[-1, 0, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 0],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1]]
```
Where 1 is available to pass, 0 is cannot pass, -1 is the initial position

Then Get a result for all solutions. In my program it calculated as:
```java
Sotution 1:
1	2	3	6	7	8
@	_	4	5	10	9
_	16	15	12	11	_
18	17	14	13	28	29
19	22	23	26	27	30
20	21	24	25	_	31
```
Go throught the numbers from 0, then you can have a path.

Enjoy!
