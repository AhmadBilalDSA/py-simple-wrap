# Easy Regex

Working with text often requires extracting specific patterns like email addresses, websites, or numbers. Writing regular expressions from scratch can be tricky and frustrating, but the `easy_regex` module provides beginner-friendly helpers that make pattern extraction simple and readable.

## A small real-world example

Imagine you're building a tool to parse a batch of user feedback messages or customer support logs, and you want to extract all submitted email addresses and website links to build a quick contact list.

```python
from py_simple import extract_emails, extract_urls

text = """
Please contact our support team at support@example.com or 
sales@test.org. You can also visit our website at [https://www.example.com](https://www.example.com) 
or check out our partner page www.test.org.
"""

emails = extract_emails(text)
urls = extract_urls(text)

print(emails)
print(urls)