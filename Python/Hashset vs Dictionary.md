It might not be clear if a `dict()` in python shares the same time complexity as a `set()`, in temrs of read / write.

I found the usage watching [this](https://www.youtube.com/watch?v=3OamzN90kPg) solution to a leetcode problem.

It entirely depends on the context of your problem. If you only need to check if a value already exists without needing to popualate the entire list, first, using a `Set()` would make more sense.  
In cases where you need to store key-value pairs, only then a dictionary is really needed.

The first example below shows a duplicacy checking code using a dictionary, which does work but really isn't very readable.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = False
        dic = {}
        for num in nums:
            if num in dic:
                dup = True
                break
            dic[num] = 1
        return dup
```

Same code with better readability having used a `set()`.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = False
        hashset = set()
        for num in nums:
            if num in hashset:
                dup = True
                break
            hashset.add(num)
        return dup
```