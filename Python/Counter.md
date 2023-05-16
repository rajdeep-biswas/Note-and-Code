Consider the following piece of code -

```python
counts = {}
for letter in sentence:
    counts[letter] = 1 + counts.get(letter, 0)
```

Using the `collections` library, it can be shortened to the following (which also somewhat improves performance) -

```python
from collections import Counter
counts = Counter(sentence)
```
