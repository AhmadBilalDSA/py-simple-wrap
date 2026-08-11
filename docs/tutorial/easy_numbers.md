# Easy Numbers

Working with numbers is central to most programs, checking if a value is even or odd, validating whether it's within range, calculating averages, or determining if a number is prime. Whether you're processing user input, analyzing data, or implementing business logic, `easy_numbers` provides beginner-friendly helpers that make numerical operations simple and readable.

## A small real-world example

Imagine you're building a rating system for a mobile app. Users can rate items from 1 to 5, but due to a data sync issue, you've collected some ratings that might be negative or out of range. Before displaying the average rating, you need to validate the data, clamp ratings to the valid range, and calculate the mean.

```python
from py_simple import clamp, average, is_positive

ratings = [-2, 4, 5, 3, 6, 4, 2]

# Clean up invalid ratings
cleaned_ratings = [clamp(r, 1, 5) for r in ratings]

# Verify all ratings are positive (they should be after clamping)
if all(is_positive(r) for r in cleaned_ratings):
    avg_rating = average(cleaned_ratings)
    print(f"Average rating: {avg_rating}")
else:
    print("Data validation failed.")
```

**Note:** This example uses Python's list comprehension syntax (`[... for ... in ...]`) to apply `clamp()` to every rating. If that's unfamiliar, you can write it as a regular loop instead. The result is the same!

```python
# Alternative beginner-friendly way:
cleaned_ratings = []
for r in ratings:
    cleaned_ratings.append(clamp(r, 1, 5))
```

Example output:

```text
Average rating: 3.43
```

## What happened?

`clamp()` constrains each rating to the 1–5 range, replacing out-of-bounds values with the nearest valid boundary. `[-2, 4, 5, 3, 6, 4, 2]` becomes `[1, 4, 5, 3, 5, 4, 2]`.

`is_positive()` checks that each clamped rating is greater than zero, ensuring data integrity.

`average()` sums all cleaned ratings and divides by the count, returning the result rounded to 2 decimal places. The average of the cleaned data (1 + 4 + 5 + 3 + 5 + 4 + 2) ÷ 7 = 3.43.

## Why use these helpers?

Instead of writing conditional logic for each validation step, manually calculating averages, or implementing range constraints yourself, you can simply write:

```python
cleaned = [clamp(r, 1, 5) for r in ratings]
if all(is_positive(r) for r in cleaned):
    avg = average(cleaned)
```

These helpers keep numerical operations simple, readable, and beginner-friendly while providing essential tools for validation, normalization, mathematical calculations, and data quality checks across integers, floats, and real-world datasets.