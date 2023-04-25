Consider the following piece of code -

```python
grouped_dict = dict()

for st in strs:
    sorted_st = ''.join(sorted(st))
    if sorted_st not in grouped_dict:
        grouped_dict[sorted_st] = []
    grouped_dict[sorted_st].append(st)

print(grouped_dict)
```

The condition checking can be omitted (or rather done in a single line of code) by using a defaultdict() -

```python
grouped_dict = defaultdict(list)

for st in strs:
    grouped_dict[''.join(sorted(st))].append(st)

print(grouped_dict)
```

Note that it is important to supply the default datatype as a parameter to defaultdict().
