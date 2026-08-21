# Working with Lists Made Easy

When processing data—like cleaning up user submissions or formatting query results—you often find yourself repeating the same boilerplate list operations. The `easy_lists` module wraps common list-wrangling tasks into simple, readable functions.

## Real-World Example: Cleaning Survey Feedback

Imagine you are managing feedback submissions from a community survey. Respondents frequently submit duplicate answers, and some entries include unwanted repetition.

Here is how you can use `easy_lists` functions together to clean, de-duplicate, and organize the feedback for review:

```python
from py_simple_wrap import easy_lists

# Raw survey responses containing duplicates
raw_responses = [
    "Great service!",
    "Needs improvement",
    "Great service!",
    "Fast delivery",
    "Needs improvement",
    "Loved the UI",
]

# Step 1: Find duplicate responses to track repeating trends
duplicates = easy_lists.find_duplicates(raw_responses)
print("Duplicate feedback found:", duplicates)

# Step 2: Get unique items for a clean final review list
unique_feedback = easy_lists.unique_items(raw_responses)
print("Unique feedback:", unique_feedback)

# Step 3: Chunk the unique feedback into pages of 2 items each
paginated_feedback = easy_lists.chunk_list(unique_feedback, 2)
print("Paginated feedback reports:", paginated_feedback)
```

## What Happened?

### 1. `find_duplicates()`

`find_duplicates(raw_responses)` identified every item that appeared more than once, such as `"Great service!"` and `"Needs improvement"`.

It keeps the order in which the duplicate items first occurred without repeating them in the output.

### 2. `unique_items()`

`unique_items(raw_responses)` removed duplicate submissions while preserving the original insertion order.

This avoids the unordered behavior of converting the list directly to a standard `set()`.

### 3. `chunk_list()`

`chunk_list(unique_feedback, 2)` divided the cleaned list into smaller sub-lists containing two items each.

This makes the feedback ready for pagination, display batches, or split reporting.

## Why Use These Helpers?

### Preserves Insertion Order

`unique_items()` keeps items in their original sequence without requiring extra boilerplate such as `dict.fromkeys()` or custom loops.

### Readable and Intent-Driven

Functions like `find_duplicates()` and `chunk_list()` make your code self-documenting compared to complex list comprehensions or nested slicing.

### Zero Boilerplate

These helpers replace repetitive tracking sets, index calculations, and boundary checks with clean, beginner-friendly one-liners.
