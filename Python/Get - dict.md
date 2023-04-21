Consider the following piece of code -

```python
dictionary = dict()
for item in arr:
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1
```

The following can be elegantly rewritten using the `get()` method available for `dict`s -

```python
dictionary = dict()
for item in arr:
    dictionary[item] = 1 + dictionary.get(item, 0)
```

This is very handy.