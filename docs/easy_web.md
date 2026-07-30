# 🌐 Easy Web

[<- Back to Main Menu](../README.md)

`easy_web` is designed to take the headache out of interacting with websites. It handles the connection checks and HTML parsing for you, so you can focus on the data.

## 🛠️ Functions

### `is_page_up(url)`
Checks if a website is currently accessible and responding normally.

- **Arguments:** `url` (str) - The full address of the website (e.g., "https://google.com").
- **Returns:** `bool` - `True` if the site is up (Status 200), `False` if there is an error or it's down.

### `get_page_content(url)`
Fetches the HTML content of a page and returns it in a "pretty" readable format.

- **Arguments:** `url` (str) - The website address to fetch.
- **Returns:** `str` or `None` - Returns the formatted HTML text if successful, or `None` if the request fails.

---

## 🚀 Quick Example

### The "Traditional" Way (Complex)
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
```

### The Py_simple Way
```python
from py_simple import easy_web

if easy_web.is_page_up("https://example.com"):
    content = easy_web.get_page_content("https://example.com")
    print(content)
```