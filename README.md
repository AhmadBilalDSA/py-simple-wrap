# Py_simple 🚀
 
**Making Python feel like plain English.**
 
[![PyPI](https://img.shields.io/pypi/v/py-simple-wrap)](https://pypi.org/project/py-simple-wrap/)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://sara-czasak.github.io/py_simple/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/sara-czasak/py_simple/blob/main/LICENSE.md)
[![GitHub stars](https://img.shields.io/github/stars/sara-czasak/py_simple?style=social)](https://github.com/sara-czasak/py_simple/stargazers)
 
Py_simple is a beginner-friendly Python wrapper package designed to help beginners and developers perform common tasks using simple, intuitive functions.
 
The goal of this project is to remove the need for memorizing complex syntax or writing repetitive boilerplate code, making Python more accessible and enjoyable for everyone.
 
```bash
pip install py-simple-wrap
```
 
```python
from py_simple import make_blank_file, miles_to_km, is_valid_email
 
make_blank_file("notes.txt")
print(miles_to_km(26.2))                    # 42.16...
print(is_valid_email("hello@example.com"))  # True
```
 
> Full walkthrough in [QUICKSTART.md](QUICKSTART.md), or browse the full **[documentation site](https://sara-czasak.github.io/py_simple/)**.
 
### ⭐ If Py_simple made something easier for you
 
Consider giving it a **star** — it helps other beginners find it, and it genuinely makes my day. And if there's a function you wish existed, **fork it** and add it; this project grew because other people did exactly that. Every module below started here, except `easy_strings`, which came from a contributor.
 
---

## 🛠️ Module Menu

Py_simple provides simple modules designed to make common Python tasks easier.

### 📂 Easy File Manager

Simplify everyday file operations with beginner-friendly utilities.

Features include:

- File management helpers
- Easier file operations
- Cleaner Python workflows

---

### 🕰️ Easy Date Formatter

Make working with dates simpler and more readable.

Features include:

- Date formatting utilities
- Easier date manipulation
- Simple date-related functions

---

### 🔢 Easy Numbers

Perform common number operations using simple and readable functions.

Features include:

- Number utilities
- Beginner-friendly calculations
- Cleaner mathematical operations

---
### 🔤 Easy Strings

Handle common string operations using clear, beginner-friendly functions.

Features include:

- Removing repeated spaces
- Converting text to `snake_case`
- Converting text to `kebab-case`
- Checking whether text is a palindrome

### 🔄 Easy Converter

Convert values easily using simple utility functions.

Features include:

- Simple conversions
- Easy-to-use helpers
- Less repetitive code

---

### ✅ Easy Validator

Validate common input formats using simple, readable functions.

Features include:

- Email, username, and URL validation
- US zip code validation
- Password strength validation

---

### 🌐 Easy Web

Make getting data from the web less complex.

Features include:

- Checking if website is up
- Getting page content

More examples and documentation will be added as the project grows.

---

## 🤝 Contributing
 
I would love to have your help in making Python simpler for everyone!
 
Contributions of all sizes are welcome:
 
- Fix documentation
- Improve existing modules
- Suggest new features
- Add new functionality
- Improve examples
Please check [CONTRIBUTING.md](https://github.com/sara-czasak/py_simple/blob/main/CONTRIBUTING.md) before submitting changes.
 
Every contribution helps make Py_simple better for beginners and developers.
 
---

## 🌟 Hall of Fame

A huge thank you to the wonderful people who have helped build Py_simple:

- **Sara Czasak** (Creator)
- **ghostfix-pm** (Major features & Refactoring)
- **jagjitkaur0000** (Added tests for easy_numbers module)
- **Onion0121** (Improved documentation)
- **averyquinnhq** (Added tests for easy_converter.py)
- **gaoharimran29-glitch** (Added tests for easy_validator.py)
- **mmaxjr** (Improved documentation)
- **sol4nki** (Expanded easy_converter.py module)
- **shivams786** (Added easy_strings.py)
- **HeaTTap** (Added tests for easy_web module)
- **Challa Leela Prasad** (Enhanced easy_strings module)
- **atiqur rahman** (Expanded unit tests for easy_strings and easy_web modules)

See the full list of contributions in [CONTRIBUTORS.md](docs/about/contributors.md).

---

## ⚖️ License

This project is licensed under the MIT License.

You are free to use, modify, and distribute it.

See the [LICENSE.md](docs/about/license.md) file for the full legal text.
