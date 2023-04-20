It might not be clear if a `dict()` in python shares the same time complexity as a `Set()`, in temrs of read / write.

I found the usage watching [this](https://www.youtube.com/watch?v=3OamzN90kPg) solution to a leetcode problem.

It entirely depends on the context of your problem. If you only need to check if a value already exists without needing to popualate the entire list, first, using a `Set()` would make more sense.  
In cases where you need to store key-value pairs, only then a dictionary is really needed.