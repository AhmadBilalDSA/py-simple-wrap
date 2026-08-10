# Easy Date Formatter

Working with dates often means remembering `strftime` formatting codes and writing the same date calculations repeatedly. The `easy_date_formatter` module provides simple helpers for getting current, past, and future dates in common formats without needing to memorize those formatting codes.

## A small real-world example

Imagine you're creating a report and want to display today's date, the date from one week ago, and the date one week from now in a readable format.

```python
from py_simple import (
    get_pretty_date,
    get_past_pretty_date,
    get_future_pretty_date,
)

today = get_pretty_date()
last_week = get_past_pretty_date(7)
next_week = get_future_pretty_date(7)

print(today)
print(last_week)
print(next_week)
```

Example output:

```text
Monday, August 10, 2026
Monday, August 03, 2026
Monday, August 17, 2026
```

## What happened?

`get_pretty_date()` returns the current date in a human-friendly format such as `Monday, August 10, 2026`.

`get_past_pretty_date()` calculates a date a specific number of days in the past and returns it in the same readable format.

`get_future_pretty_date()` does the same thing for a date in the future.

The module also provides common formats such as `DD-MM-YYYY`, `MM-DD-YYYY`, `DD/MM/YYYY`, and `MM/DD/YYYY`.

For example:

```python
from py_simple import dd_mm_yyyy, slash_dd_mm_yyyy

print(dd_mm_yyyy())
print(slash_dd_mm_yyyy())
```

Example output:

```text
10-08-2026
10/08/2026
```

You can also use `list_available_formats()` to see which formats are supported:

```python
from py_simple import list_available_formats

print(list_available_formats())
```

## Why use these helpers?

Instead of remembering `strftime` codes and repeatedly writing date calculations, you can simply use:

```python
today = get_pretty_date()
last_week = get_past_pretty_date(7)
next_week = get_future_pretty_date(7)
```

These helpers keep working with dates simple, readable, and beginner-friendly while providing several common date formats and easy ways to calculate past and future dates.