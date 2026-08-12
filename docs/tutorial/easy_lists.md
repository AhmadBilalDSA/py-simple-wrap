# Easy Lists

Working with lists is one of the most common things you'll do in Python. Removing duplicates, finding repeated items, splitting lists, sorting values, and combining lists are all operations that can require repetitive code.

The `easy_lists` module provides simple helpers for common list operations, making them easier to use without writing the underlying logic yourself.

## A small real-world example

Imagine you're processing a list of values from an application. You want to remove duplicates, split the data into smaller groups, and sort the results.

```python id="2z8q5r"
from py_simple import unique_items, chunk_list, sort_numbers

numbers = [5, 2, 5, 8, 2, 1, 9]

numbers = unique_items(numbers)
numbers = sort_numbers(numbers)

chunks = chunk_list(numbers, 2)

print(numbers)
print(chunks)
```

Example output:

```text id="k0qz5n"
[1, 2, 5, 8, 9]
[[1, 2], [5, 8], [9]]
```

## What happened?

`unique_items()` removes duplicate values while keeping their original order.

`find_duplicates()` finds the values that appear more than once.

`chunk_list()` splits a list into smaller lists of the size you specify.

`flatten_list()` removes one level of nested lists.

`most_common_item()` finds the value that appears most frequently.

You can also rotate, merge, alternate, sum, and sort lists:

```python id="n6z7k1"
from py_simple import (
    rotate_list,
    merge_lists,
    alternate_lists,
    sum_all
)

print(rotate_list([1, 2, 3], 1))
# [3, 1, 2]

print(merge_lists([1, 2], [3, 4]))
# [1, 2, 3, 4]

print(alternate_lists([1, 2], [3, 4]))
# [1, 3, 2, 4]

print(sum_all([1, [2, 3], 4]))
# 10
```

## The Py_simple Way

```python id="q0k6jc"
from py_simple import (
    unique_items,
    find_duplicates,
    chunk_list,
    flatten_list,
    most_common_item,
    rotate_list,
    merge_lists,
    alternate_lists,
    sum_all,
    sort_numbers,
    sort_words
)

numbers = [3, 1, 2, 2, 4, 3]

print(unique_items(numbers))
print(find_duplicates(numbers))
print(chunk_list(numbers, 2))
print(flatten_list([[1, 2], [3, 4]]))
print(most_common_item(numbers))
print(rotate_list(numbers, 2))
print(merge_lists([1, 2], [3, 4]))
print(alternate_lists([1, 2], [3, 4]))
print(sum_all([1, [2, 3], 4]))
print(sort_numbers(numbers))
print(sort_words(["banana", "Apple", "cherry"]))
```

## The Traditional Way

Without `py_simple`, many of these operations require writing the logic yourself or combining several built-in Python features:

```python id="8rq3fp"
from collections import Counter

numbers = [3, 1, 2, 2, 4, 3]

# Remove duplicates
unique = []
for item in numbers:
    if item not in unique:
        unique.append(item)

# Find duplicates
duplicates = []
for item in numbers:
    if numbers.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

# Split into chunks
size = 2
chunks = [
    numbers[i:i + size]
    for i in range(0, len(numbers), size)
]

# Find the most common item
most_common = Counter(numbers).most_common(1)[0][0]

# Sort numbers
sorted_numbers = sorted(numbers)

# Sort words alphabetically
words = ["banana", "Apple", "cherry"]
sorted_words = sorted(words, key=str.lower)
```

The `easy_lists` helpers package these common patterns into simple, reusable functions.

## Working with nested lists

`flatten_list()` can turn a list containing nested lists into a single-level list.

```python id="g4r8xw"
from py_simple import flatten_list

result = flatten_list([
    [1, 2],
    [3, 4],
    5
])

print(result)
```

Output:

```text id="4hm5d7"
[1, 2, 3, 4, 5]
```

`sum_all()` uses the same idea to add numbers contained inside nested lists:

```python id="v5v4ym"
from py_simple import sum_all

print(sum_all([1, [2, 3], [4, 5]]))
```

Output:

```text id="6pxf9b"
15
```

## Sorting lists

`sort_numbers()` sorts numbers from smallest to largest:

```python id="j0c1gk"
from py_simple import sort_numbers

print(sort_numbers([5, 1, 8, 2]))
```

Output:

```text id="x5k7x3"
[1, 2, 5, 8]
```

`sort_words()` sorts words alphabetically while ignoring differences in capitalization:

```python id="x0a8jv"
from py_simple import sort_words

print(sort_words(["banana", "Apple", "cherry"]))
```

Output:

```text id="c3v1rm"
["Apple", "banana", "cherry"]
```

## Combining lists

`merge_lists()` combines two lists:

```python id="s4j9pf"
from py_simple import merge_lists

print(merge_lists([1, 2], [3, 4]))
```

Output:

```text id="2h6g6s"
[1, 2, 3, 4]
```

`alternate_lists()` combines two lists by taking one item from each list at a time:

```python id="n1q5fd"
from py_simple import alternate_lists

print(alternate_lists([1, 2], [3, 4]))
```

Output:

```text id="f3k8q2"
[1, 3, 2, 4]
```

## Why use these helpers?

Instead of repeatedly writing loops, comprehensions, sorting logic, and list manipulation code, you can simply use:

```python id="w9h3kf"
unique_items(items)
find_duplicates(items)
chunk_list(items, 2)
flatten_list(items)
most_common_item(items)
rotate_list(items, 1)
merge_lists(list_a, list_b)
alternate_lists(list_a, list_b)
sum_all(items)
sort_numbers(items)
sort_words(items)
```

These helpers keep common list operations simple, readable, and beginner-friendly while handling the underlying loops, indexing, sorting, and list manipulation for you.
