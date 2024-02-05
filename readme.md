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
  
Also, just had this feeling that DFS is similar in spirit to pre-order traversal, [which is indeed true](https://softwareengineering.stackexchange.com/questions/227779/is-pre-order-traversal-same-as-depth-first-search), just that "traversal" and "search" have different purposes.

#### 5th September
/Python: It's entirely possible to compared nested lists / tuples with the `==` operator. As below example
```python3
[('root', None), ('left', 3)] == [('root', None), ('left', 3)] # returns True
```
  
/DSA: If the recursive solutions to trees are not making intuitive sense, to convert them into iterative solutions, the idea is that they will need a stack (if the solution is DFS) or they will need a queue (if the solution is BFS).

#### 6th September
/DSA: In-order traversal is how you get elements out of a BST in sorted-order.

#### 19th September
/DSA: Especially in the context of trees, I need to remember / learn patterns. For example, I had solved `100. Same Tree` back on 5th September, but by 19th Sept, when I was attemping `572. Subtree of Another Tree`, I entirely forgot that implementation and went back to my default "compare in-order traversals to check if they're equal" approach.  

Also, turns out, if I add my own test case of inputs to #573 on leetcode (which is actually inspired by a corner case on #100) -
```shell
root = [3,1,5,2,2,null,2,2,null,2]
subRoot = [1,2,2,2,null,null,2]
```
It will still get accepted as a submission but fail this custom testcase. That's hilarious and I am thinking of submitting this corner case.

#### 21st September
/Python: `collections.deque` is implemented as a doubly-linked list. Queue operations like popleft and append are efficient, with an average time complexity of O(1). On the other hand, I have been using `queue.insert(0, node)` to simulate a queue operation where elements are added at the beginning of the list, which has a time complexity of O(N) because it requires shifting all existing elements to make room for the new element.

#### 25th September
/Python: If you're updating a list variable with sublists via another variable, make sure to use `sublist.copy()` because if you directly use `mainlist.append(sublist)`, any subsequent modifications to the sublist will also reflect in previously appended sublists and the final main list will be just full of the final sublist. See `Leetcode/78. Subsets.py` for example.

#### 26th September
/DSA: Iterative binary search becomes very, very intuitive as soon as you start thinking in a two-pointer visual approach and not just the numbers.  
Also (this is a bit obvious but), it's important to set the condition to `while l <= r` and not `while l < r` since they might overlap at the last element that might be our answer.

#### 30th September
/DSA: Cleaner Boolean logic in python. `True if x else y` can be rewritten as `x or y`.

#### 15th November
/DSA: Leetcode 70. Climbing Stairs is just Fibonacci. [As discussed here](https://dev.to/alisabaj/the-climbing-staircase-problem-how-to-solve-it-and-why-the-fibonacci-numbers-are-relevant-3c4o).

#### 16th November
/DSA / Leetcode: Using a member variable cache can help in boosting performance further because it is going to be used across testcases. 🤯
PS: the very thing that used to cause problems and had to be manually reset is helping here.

#### 5th Feb
/Python: Syntax for sorting based on sublist index with lambda function `intervals.sort(key=lambda pair: pair[0])`.
