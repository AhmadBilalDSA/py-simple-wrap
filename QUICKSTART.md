<div align="center">

[README](README.md) · [Modules](MODULES.md) · [Support](SUPPORT.md) · [Contributing](CONTRIBUTING.md) · [Contributors](CONTRIBUTORS.md) · [Changelog](CHANGELOG.md) · [Security](SECURITY.md) · [Code of Conduct](CODE_OF_CONDUCT.md) · [License](LICENSE.md)

</div>

# Quickstart
 
Get up and running with `py-simple-wrap` in under a minute.
 
## Installation
 
```bash
pip install py-simple-wrap
```
 
> **Note:** The PyPI package is named `py-simple-wrap` (the name `py-simple` was already taken), but you still import it as `py_simple` in your code.
 
## Basic Usage
 
Every function is available directly from the top-level package — no need to dig into submodules:
 
```python
from py_simple import make_blank_file, miles_to_km, is_valid_email
 
# Create a new file in one line
make_blank_file("notes.txt")
 
# Convert units without memorizing formulas
distance_km = miles_to_km(26.2)
print(distance_km)  # 42.16...
 
# Validate common input formats
print(is_valid_email("hello@example.com"))  # True
```
 
## A Taste of Each Module
 
### 📂 File handling — `easy_file_manager`
 
```python
from py_simple import make_blank_file, add_a_line, read_file_to_list
 
make_blank_file("todo.txt")
add_a_line("todo.txt", "Buy groceries")
print(read_file_to_list("todo.txt"))
```
 
### 🕰️ Dates — `easy_date_formatter`
 
```python
from py_simple import get_pretty_date, dd_mm_yyyy
 
print(get_pretty_date())     # e.g. "July 31, 2026"
print(dd_mm_yyyy())          # e.g. "31-07-2026"
```
 
### 🔄 Unit conversion — `easy_converter`
 
```python
from py_simple import celsius_to_fahrenheit, kg_to_lb
 
print(celsius_to_fahrenheit(20))  # 68.0
print(kg_to_lb(70))               # 154.32...
```
 
### 🔢 Numbers — `easy_numbers`
 
```python
from py_simple import is_prime, average
 
print(is_prime(17))          # True
print(average([4, 8, 15, 16, 23, 42]))
```
 
### ✅ Validation — `easy_validator`
 
```python
from py_simple import is_password_secure, is_valid_url
 
print(is_password_secure("hunter2"))          # False
print(is_valid_url("https://example.com"))    # True
```
 
### 🌐 Web — `easy_web`
 
```python
from py_simple import is_page_up, get_page_content
 
print(is_page_up("https://python.org"))  # True
```
 
### 🔤 Strings — `easy_strings`
 
```python
from py_simple import to_snake_case, is_palindrome
 
print(to_snake_case("Hello World"))  # "hello_world"
print(is_palindrome("racecar"))      # True
```
 
## Next Steps
 
- Browse the **Reference** section in the sidebar for the complete list of functions in every module.
- See the full [README](docs/readme.md) for the complete list of functions in each module.
- Want to contribute? Check out [CONTRIBUTING.md](docs/how-to/contributing.md).

<div align="center">

## **INDEX**

| <div style="width:200px">File</div> | <div style="width:680px">What's in it</div>                         | <div style="width:150px">File</div>      |
|:------------------------------------|:--------------------------------------------------------------------|:-----------------------------------------|
| 📜 CHANGELOG                        | Every notable change, release by release.                           | [CHANGELOG.md](CHANGELOG.md)             |
| 🌱 CODE_OF_CONDUCT                  | The ground rules for a respectful, beginner-safe community.         | [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) |
| 🚀 CONTRIBUTING                     | Step-by-step guide to making your first (or fiftieth) contribution. | [CONTRIBUTING.md](CONTRIBUTING.md)       |
| 🌟 CONTRIBUTORS                     | Everyone who's helped build this, sorted into guilds.               | [CONTRIBUTORS.md](CONTRIBUTORS.md)       |
| ⚖️ LICENSE                          | MIT license — what you're allowed to do with this code.             | [LICENSE.md](LICENSE.md)                 |
| 📦 MODULES                          | Every module at a glance, grouped by what it removes.               | [MODULES.md](MODULES.md)                 |
| 🏠 README                           | The landing page — what py-simple-wrap is and why it exists.        | [README.md](README.md)                   |
| 🔒 SECURITY                         | How to privately report a vulnerability.                            | [SECURITY.md](SECURITY.md)               |
| 🆘 SUPPORT                          | Where to go when you're stuck or have a question.                   | [SUPPORT.md](SUPPORT.md)                 |

</div>
<br>