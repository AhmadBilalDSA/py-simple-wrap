# Easy Regex

Working with text often requires extracting specific patterns like email addresses, websites, or numbers. Writing regular expressions from scratch can be tricky and frustrating, but the `easy_regex` module provides beginner-friendly helpers that make pattern extraction simple and readable.

## A Small Real-World Example

Imagine you're building a tool to parse a batch of user feedback messages or customer support logs. You want to extract all submitted email addresses and website links to build a quick contact list.

```python
from py_simple import extract_emails, extract_urls

text = """
Please contact our support team at support@example.com or
sales@test.org. You can also visit our website at https://www.example.com
or check out our partner page www.test.org.
"""

emails = extract_emails(text)
urls = extract_urls(text)

print(emails)
print(urls)
```

## What Happened?

`extract_emails()` scans the text and returns a list of all valid email addresses found.

`extract_urls()` scans the text and identifies web addresses, including URLs that start with `http://`, `https://`, or `www.`.

Instead of writing regular expressions manually, you can call these helpers directly with the text you want to search:

```python
emails = extract_emails(text)
urls = extract_urls(text)
```

The results are returned as lists that are ready to use in your program.

## Why Use These Helpers?

Writing regular expressions from scratch can be difficult because you need to create, test, and maintain complex patterns. The `easy_regex` helpers handle this complexity for you.

Using these helpers makes your code:

- **Simple** – No need to write complex regex patterns.
- **Readable** – The function names clearly describe what they do.
- **Reusable** – Use the same helpers whenever you need to extract emails or URLs.
- **Beginner-friendly** – Focus on solving your problem instead of learning complicated regex syntax.

For example:

```python
emails = extract_emails(text)
urls = extract_urls(text)
```

This is much easier to understand than writing and maintaining the regular expression patterns yourself.