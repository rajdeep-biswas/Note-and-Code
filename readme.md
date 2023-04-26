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
