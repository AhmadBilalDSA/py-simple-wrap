# Easy Stats

Working with statistics is common when analyzing data, tracking performance, or making informed decisions. Whether you're finding the middle value of a dataset, understanding how spread out numbers are, or identifying percentile ranks, `easy_stats` provides beginner-friendly helpers that make statistical operations simple and readable.

## A small real-world example

Imagine you're a teacher who just gave a quiz to your class. You want to quickly understand the overall performance: What's the typical score? How much do scores vary? What's the full range? Before uploading grades, you need a quick statistical summary.

```python
from py_simple import median, standard_deviation, data_range

scores = [65, 72, 78, 81, 85, 88, 92]

# Get key statistics about the performance
middle_score = median(scores)
spread = standard_deviation(scores)
score_range = data_range(scores)

print(f"Median score: {middle_score}")
print(f"Standard deviation: {spread}")
print(f"Score range: {score_range}")
```

Example output:

```text
Median score: 81
Standard deviation: 9.37
Score range: 27
```

**Note:** This example uses Python's list comprehension syntax (`[... for ... in ...]`) to apply functions to data. If that's unfamiliar, you can use the functions one at a time instead. The result is the same!

```python
# Alternative beginner-friendly way:
scores = [65, 72, 78, 81, 85, 88, 92]
middle_score = median(scores)
spread = standard_deviation(scores)
score_range = data_range(scores)
```

## What happened?

`median()` finds the middle value when scores are arranged in order. With 7 scores, it returns the 4th value: 81.

`standard_deviation()` measures how spread out the scores are from the average. A value of 9.37 means scores typically vary by about 9 points from the mean. This helps you see if the class performed consistently or if there's a wide gap between top and bottom performers.

`data_range()` shows the difference between the highest and lowest scores: 92 - 65 = 27. This gives you the total span of performance at a glance.

## Why use these helpers?

Instead of writing complex logic to sort data, calculate averages, or implement statistical formulas yourself, you can simply write:

```python
middle = median(scores)
spread = standard_deviation(scores)
range_val = data_range(scores)
```

These helpers keep statistical analysis simple, readable, and beginner-friendly while providing essential tools for data summarization, performance tracking, and understanding data distributions without needing deep mathematical knowledge.