Consider a simple iteration via indices -

```python
for i in range(len(arr)):
    print(i, arr[i])
```

There is a slightly more elegant way to write the the above using `enumerate()` -

```python
for i, ele in enumerate(arr):
    print(i, ele)
```
