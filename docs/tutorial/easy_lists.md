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
    "Loved the UI"
]

# Step 1: Find duplicate responses to track repeating trends
duplicates = easy_lists.find_duplicates(raw_responses)
print("Duplicate feedback found:", duplicates)

# Step 2: Get unique items for a clean final review list
unique_feedback = easy_lists.unique_items(raw_responses)
print("Unique feedback:", unique_feedback)

# Step 3: Chunk the unique feedback into pages of 2 items each for the report
paginated_feedback = easy_lists.chunk_list(unique_feedback, 2)
print("Paginated feedback reports:", paginated_feedback)