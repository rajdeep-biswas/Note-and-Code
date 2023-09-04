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

#### 7th August
/Python: You can sort a list of Objects by the attributes via using the key parameter along with a `lambda` function.  
[Stackoverflow explanation](https://stackoverflow.com/questions/403421/how-do-i-sort-a-list-of-objects-based-on-an-attribute-of-the-objects).

#### 12th August
/DSA. Quick TIL: In case of a sorted array, if you're trying to insert a new element (while maintaining sorted order, of course), while you can identify the appropriate index at O(logn) via binary search, however, actually inserting the element into said position will be O(n) since you'll have to move over all the following elements.  
The latter wasn't making sense why shouldn't it be O(logn) as well? (originating from Neetcode's heap usage [perfectly timestamped here!](https://youtu.be/hOjcdrqMoQ8?t=159).), and then it quickly clicked why inserting is a significantly different operation compared to identifying the index.

#### 25th August
/Leetcode: The `Editorial` section on any problem (free for most problems, I guess?) is actually the "Official Solution(s)" section and often the best place to start.  
For example, each of [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/editorial) and [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/editorial) solutions were progressively intuitive and really well documented.

#### 4th September
/DSA Tip: In your [DSA Map Excel](https://docs.google.com/spreadsheets/d/15YePlUbNrcXYa6QndV0GTpUwqDhjNEpUzbQ9aUKaj2U/edit#gid=0) group problems that have similar solution patterns together, like [Neetcode mentions in his video](https://youtu.be/SVvr3ZjtjI8?si=K5zkXYLz70Mh-8Dh&t=270), DP problems have similar patterns, multiple tree problems use (recursive) BFS, etc.
