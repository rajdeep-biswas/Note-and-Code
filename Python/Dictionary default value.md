Consider you have the following code -

```python3
node_hash = {}
while ctrav:
    ctrav.random = node_hash[trav.random] if trav.random != None else None
```

The additional conditional is required to deal with cases there trav.random might result in None, think trav is a node of a linkedlist and its random pointer points to null.

In that case, there is a more elegant way to rewrite this via a default initialization of None into the dictionary -

```python3
node_hash = {None: None}
while ctrav:
    ctrav.random = node_hash[trav.random]
```
