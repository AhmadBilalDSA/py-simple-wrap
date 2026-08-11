# Easy Regex

Regular expressions are powerful for finding patterns inside text, but writing the correct pattern can be difficult, especially when you only need to extract common types of data.

The `easy_regex` module provides simple helpers for extracting emails, URLs, numbers, and number sequences from text without writing the underlying regular expressions yourself.

## A small real-world example

Imagine you're processing a log file or a text message and need to find contact information and numerical data.

```python
from py_simple import extract_emails, extract_urls, extract_numbers

text = """
Contact admin@example.com or visit https://example.com.
The server received 42 requests and returned 200.
"""

emails = extract_emails(text)
urls = extract_urls(text)
numbers = extract_numbers(text)

print(emails)
print(urls)
print(numbers)
```

Example output:

```text
['admin@example.com']
['https://example.com']
['42', '200']
```

## What happened?

`extract_emails()` finds email addresses inside a piece of text.

`extract_urls()` finds URLs, including URLs beginning with `http://`, `https://`, or `www.`.

`extract_numbers()` extracts standalone sequences of digits.

`extract_number_sequences()` finds numbers connected by separators such as `-`, `_`, `:`, or `.`, which can be useful for dates, times, IP addresses, version numbers, and similar values.

For example:

```python
from py_simple import extract_number_sequences

text = "Server 192.168.1.1 logged in at 14:32 on 04-08-2026"

print(extract_number_sequences(text))
```

Output:

```text
['192.168.1.1', '14:32', '04-08-2026']
```

## The Py_simple Way

```python
from py_simple import (
    extract_emails,
    extract_urls,
    extract_number_sequences,
    extract_numbers
)

text = """
Email: hello@example.com
Website: https://example.com
Server: 192.168.1.1
Requests: 42
"""

print(extract_emails(text))
print(extract_urls(text))
print(extract_number_sequences(text))
print(extract_numbers(text))
```

## The Traditional Way

Without `py_simple`, you would normally have to import `re` and write the appropriate regular expression yourself:

```python
import re

text = """
Email: hello@example.com
Website: https://example.com
Server: 192.168.1.1
Requests: 42
"""

email_pattern = r'[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+'
emails = re.findall(email_pattern, text)

number_pattern = r'[0-9]+'
numbers = re.findall(number_pattern, text)
```

For more complex patterns, such as URLs or number sequences, the regular expressions can become significantly harder to write and understand.

The `easy_regex` helpers package these common patterns into simple, reusable functions.

## Extracting emails

`extract_emails()` finds email addresses contained in a string.

```python
from py_simple import extract_emails

text = "Contact us at hello@example.com or support@test.org"

print(extract_emails(text))
```

Output:

```text
['hello@example.com', 'support@test.org']
```

If no email addresses are found, the function returns an empty list:

```python
print(extract_emails("No email addresses here."))
```

Output:

```text
[]
```

## Extracting URLs

`extract_urls()` finds common URLs in text.

```python
from py_simple import extract_urls

text = "Visit https://www.example.com or www.test.org today"

print(extract_urls(text))
```

Output:

```text
['https://www.example.com', 'www.test.org']
```

This is useful when processing messages, documents, logs, or other text containing web addresses.

## Extracting numbers

`extract_numbers()` finds standalone sequences of digits:

```python
from py_simple import extract_numbers

text = "I have 3 cats and 12 fish"

print(extract_numbers(text))
```

Output:

```text
['3', '12']
```

The values are returned as strings because they are extracted directly from the original text.

## Extracting number sequences

`extract_number_sequences()` detects groups of numbers connected by separators.

```python
from py_simple import extract_number_sequences

text = "IP: 192.168.1.1, time: 14:32, date: 04-08-2026"

print(extract_number_sequences(text))
```

Output:

```text
['192.168.1.1', '14:32', '04-08-2026']
```

This can be useful for extracting values such as:

* IP addresses
* Dates
* Times
* Version numbers
* Numeric IDs

## Why use these helpers?

Instead of repeatedly writing regular expressions for common text patterns, you can simply use:

```python
extract_emails(text)
extract_urls(text)
extract_number_sequences(text)
extract_numbers(text)
```

These helpers keep common text-extraction tasks simple, readable, and beginner-friendly while handling the underlying regular expressions for you.
