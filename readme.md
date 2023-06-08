#### 20th April
/Python: There is no time complexity difference between a `set()` and a `dict()`. It's context dependent which one you'd want to use.

#### 21st April
/Python: Using `enumerate()` is a slightly more elegant way to iterate through the indices of an iteratble.
/Engineering: Anagram problem can use a simple check upfront if the string lengths are matching. Good engineering practices like these can save you computation.
/Python: Using `get()` with dictionaries is very handy. Especially, in cases where you're trying iterate through a list to get frequency of its elements, etc.

#### 25th April
/Python: Using `defaultdict()` instead of `dict()` lets you avoid a check during populating keys via iteration.

#### 26th April
/Python: You shouldn't use the following syntax in Python if you intend to populate the sublist items independently.
```python
count = [[]] * len(arr)
```
That would create copies of the nested item, **only as long as the sublist item type is mutable**, and any changes you make to it would reflect across all the other copies.
[Explanation is provided in this stackoverflow](https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly).

#### 7th May
/DSA: Once you have solved 1. Two Sum and 167. Two Sum II, you can draw the intuition for 15. 3Sum, that you can sort the array first and then use one element as anchor to find the remaining to elements via a two-pointer approach.

#### 16th May
/Python: Usage of `collections.Counter` to easily get a frequency map of all elements in a list or string.

#### 30th May
/DSA: BFS uses a Queue. DFS uses a Stack.
In Python, the difference can be achieved by using `queue.insert(0, (r, c))` and `stack.append((r, c))`, paired with `.pop()`.

```c
# Stack push -
stack.append((r, c))

# Stack pop -
r, c = stack.pop()

# Enqueue -
queue.insert(0, (r, c))

# Dequeue -
r, c = queue.pop()
```

#### 8th June
/DSA: Learned an important detail about standard BFS implementation; recorded in `Python/standard_bfs.md`.