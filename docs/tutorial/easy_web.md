# Easy Web

Working with websites often involves several steps before you can extract useful information. The `easy_web` module provides beginner-friendly helpers that make common web tasks simple and easy to read.

## A small real-world example

Imagine you want to check whether a website is available before collecting some basic information about it.

```python
from py_simple import is_page_up, get_page_title, count_links

url = "https://github.com"

if is_page_up(url):
    print("The website is online!")

    print(get_page_title(url))
    print(count_links(url))
else:
    print("The website is unavailable.")
```

Example output:

```text
The website is online!
GitHub · Build and ship software on a single, collaborative platform · GitHub
144
```

## What happened?

`is_page_up()` checks whether the website is available before doing anything else.

`get_page_title()` retrieves the title of the page, making it easy to identify the website you're working with.

`count_links()` counts all the links on the page without requiring you to parse the HTML yourself.

## Why use these helpers?

These helpers let you focus on the information you want instead of writing the same networking and HTML parsing code every time.

```python
if is_page_up(url):
    print(get_page_title(url))
    print(count_links(url))
```

This keeps your code simple, readable, and beginner-friendly.
