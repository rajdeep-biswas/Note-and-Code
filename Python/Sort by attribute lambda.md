Say you were trying to solve [this problem](https://www.lintcode.com/problem/920/description), and you need to sort some objects in a list by one of their properties.  
You can do the following -

```python
intervals.sort(key = lambda x: x.start)
```