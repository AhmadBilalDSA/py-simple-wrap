# py-simple-wrap 🚀
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-18-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

**Making Python feel like plain English.**

[![PyPI](https://img.shields.io/pypi/v/py-simple-wrap?style=for-the-badge)](https://pypi.org/project/py-simple-wrap/)
[![Docs](https://img.shields.io/badge/docs-online-blue?style=for-the-badge)](https://sara-czasak.github.io/py-simple-wrap/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://github.com/sara-czasak/py-simple-wrap/blob/main/LICENSE.md)
[![GitHub stars](https://img.shields.io/github/stars/sara-czasak/py-simple-wrap?style=for-the-badge)](https://github.com/sara-czasak/py-simple-wrap)

py-simple-wrap is a beginner-friendly Python wrapper package designed to help beginners and developers perform common tasks using simple, intuitive functions.

The goal of this project is to remove the need for memorizing complex syntax or writing repetitive boilerplate code, making Python more accessible and enjoyable for everyone.

## You'll love py-simple-wrap if:
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=900&pause=30&color=5E7CF7&background=FF000000&multiline=true&width=1020&height=100&lines=*+You're+learning+Python+and+want+to+do+useful+things+without+memorizing+complex+syntax.;*+You're+a+developer+who's+tired+of+writing+the++same+8+lines+of+code+when+1+will+do.;*+You're+teaching+Python+and+want+students+to++focus+on+logic%2C+not+boilerplates.)](https://git.io/typing-svg)

## Before and After
### 😰 The traditional way

```python
import requests
from bs4 import BeautifulSoup

try:
    response = requests.get('https://github.com', timeout=10)
    response.raise_for_status()
    page = BeautifulSoup(response.content, 'html.parser')
    title = page.title.string
except Exception as e:
    print("The site is down or address is invalid.")
```
### 😎 The py-simple-wrap way
```python
from py_simple import get_page_title

print(get_page_title("https://github.com"))
```

## 🛠️ Installation

```bash
pip install py-simple-wrap
```

```python
from py_simple import make_blank_file, miles_to_km, is_valid_email

make_blank_file("notes.txt")
print(miles_to_km(26.2))                    # 42.16...
print(is_valid_email("hello@example.com"))  # True
```

> Full walkthrough in [QUICKSTART.md](QUICKSTART.md), or browse the full **[documentation site](https://sara-czasak.github.io/py-simple-wrap/)**.

## ⭐ If py-simple-wrap made something easier for you

Consider giving it a **star** — it helps other beginners find it, and it genuinely makes my day. And if there's a function you wish existed, **fork it** and add it; this project grew because other people did exactly that. Every module below started here, except `easy_strings`, which came from a contributor.

---

## 🛠️ Module Menu

py-simple-wrap provides simple modules designed to make common Python tasks easier.

### 📂 Easy File Manager

<details>
<summary>Click to expand — file operations without the <code>os</code> boilerplate</summary>

<br>

| Function                             | What it does                        |
|--------------------------------------|-------------------------------------|
| `make_blank_file("notes", "txt")`    | Create an empty file                |
| `is_file_there("notes.txt")`         | Check if a file exists              |
| `add_a_line("notes.txt", "hello!")`  | Append a line to a file             |
| `read_file_to_list("notes.txt")`     | Read lines into a list              |
| `remove_file("notes.txt")`           | Delete a file                       |
| `rename_file("old.txt", "new.txt")`  | Rename a file                       |
| `copy_file("src.txt", "dst.txt")`    | Copy a file                         |
| `list_files()` / `list_files("txt")` | List files, optionally by extension |

</details>

### 🕰️ Easy Date Formatter

<details>
<summary>Click to expand — readable dates without memorizing strftime codes</summary>

<br>

**Get the current date in any format:**

| Function             | Example output          |
|----------------------|-------------------------|
| `get_pretty_date()`  | `Friday, July 31, 2026` |
| `dd_mm_yyyy()`       | `31-07-2026`            |
| `mm_dd_yyyy()`       | `07-31-2026`            |
| `slash_dd_mm_yyyy()` | `31/07/2026`            |
| `slash_mm_dd_yyyy()` | `07/31/2026`            |

**Need past or future dates?** Add `past_` or `future_` to any function above and pass the number of days:

| Pattern               | Example                                    |
|-----------------------|--------------------------------------------|
| `past_<format>(7)`    | `past_pretty_date(7)` → one week ago       |
| `future_<format>(30)` | `future_dd_mm_yyyy(30)` → 30 days from now |

**Also available:** `list_available_formats()` to see all supported format names.

</details>

### 🔢 Easy Numbers

<details>
<summary>Click to expand — number checks and calculations without the mental math</summary>

<br>

| Function                        | What it does                             | Example                                 |
|---------------------------------|------------------------------------------|-----------------------------------------|
| `is_even(n)`                    | Check if a number is even                | `is_even(90)` → `True`                  |
| `is_odd(n)`                     | Check if a number is odd                 | `is_odd(67)` → `True`                   |
| `is_positive(n)`                | Check if a number is positive            | `is_positive(90)` → `True`              |
| `is_negative(n)`                | Check if a number is negative            | `is_negative(-10)` → `True`             |
| `is_prime(n)`                   | Check if a number is prime               | `is_prime(2)` → `True`                  |
| `is_evenly_divisible(n, d)`     | Check if `n` divides evenly by `d`       | `is_evenly_divisible(90, 9)` → `True`   |
| `average(nums)`                 | Average of a list, rounded to 2 decimals | `average([1.5, 2, 3])` → `2.17`         |
| `percentage_of(n, p)`           | Get a percentage of a number             | `percentage_of(100, 0.5)` → `50.0`      |
| `round_to_nearest(n, m)`        | Round to the nearest multiple            | `round_to_nearest(23, 5)` → `25.0`      |
| `greatest_common_divisor(a, b)` | Find the GCD of two numbers              | `greatest_common_divisor(12, 18)` → `6` |
| `clamp(n, min, max)`            | Keep a number within a range             | `clamp(15, 0, 10)` → `10`               |

</details>

### 📋 Easy Lists

<details>
<summary>Click to expand — list helpers that keep your code short and readable</summary>

<br>

| Function                          | What it does                             | Example                                                    |
|-----------------------------------|------------------------------------------|------------------------------------------------------------|
| `unique_items(items)`             | Remove duplicates, keeping order         | `unique_items([1, 2, 2, 3])` → `[1, 2, 3]`                 |
| `find_duplicates(items)`          | Find items that appear more than once    | `find_duplicates([1, 2, 2, 3, 3, 3])` → `[2, 3]`           |
| `chunk_list(items, size)`         | Split a list into smaller lists          | `chunk_list([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]` |
| `flatten_list(items)`             | Flatten nested lists one level deep      | `flatten_list([[1, 2], [3]])` → `[1, 2, 3]`                |
| `most_common_item(items)`         | Find the most frequent item              | `most_common_item([1, 1, 2])` → `1`                        |
| `rotate_list(items, steps)`       | Rotate items to the right                | `rotate_list([1, 2, 3], 1)` → `[3, 1, 2]`                  |
| `merge_lists(list_a, list_b)`     | Combine two lists                        | `merge_lists([1, 2], [3, 4])` → `[1, 2, 3, 4]`             |
| `alternate_lists(list_a, list_b)` | Combine lists by taking turns            | `alternate_lists([1, 2], [3, 4])` → `[1, 3, 2, 4]`         |
| `sum_all(items)`                  | Add up numbers, even in nested lists     | `sum_all([1, [2, 3], 4])` → `10`                           |
| `sort_numbers(items)`             | Sort numbers smallest to largest         | `sort_numbers([3, 1, 2])` → `[1, 2, 3]`                    |
| `sort_words(items)`               | Sort words alphabetically, ignoring case | `sort_words(["banana", "Apple"])` → `["Apple", "banana"]`  |

</details>

### 🔤 Easy Strings

<details>
<summary>Click to expand — string operations that read like English</summary>

<br>

| Function                    | What it does                               | Example                                                      |
|-----------------------------|--------------------------------------------|--------------------------------------------------------------|
| `remove_extra_spaces(text)` | Strip leading, trailing, and double spaces | `remove_extra_spaces("  hello   world  ")` → `"hello world"` |
| `to_snake_case(text)`       | Convert to snake_case                      | `to_snake_case("Hello World")` → `"hello_world"`             |
| `to_kebab_case(text)`       | Convert to kebab-case                      | `to_kebab_case("Hello World")` → `"hello-world"`             |
| `is_palindrome(text)`       | Check if text reads the same backwards     | `is_palindrome("Never odd or even")` → `True`                |
| `is_alphanumeric(text)`     | Check if text is letters and numbers only  | `is_alphanumeric("Something123")` → `True`                   |
| `count_words(text)`         | Count the number of words                  | `count_words("Hello world! How are you?")` → `5`             |

</details>

### ✂️ Easy Text

<details>
<summary>Click to expand — text formatting helpers that read like English</summary>

<br>

|------------------------------|---------------------------------------------|---------------------------------------------------------------|
| Function                     | What it does                                | Example                                                       |
| `truncate(text, length)`     | Shorten text and add an ellipsis            | `truncate("Hello world!", 5)` → `"Hello…"`                    |
| `remove_punctuation(text)`   | Strip punctuation, keep letters and numbers | `remove_punctuation("Hello, world!")` → `"Hello world"`       |
| `reverse_words(text)`        | Reverse the order of words                  | `reverse_words("Hello world")` → `"world Hello"`              |
| `capitalize_title(text)`     | Capitalize the first letter of each word    | `capitalize_title("the great gatsby")` → `"The Great Gatsby"` |
| `count_letters(text)`        | Count the number of letters                 | `count_letters("Hello 123!")` → `5`                           |
| `count_digits(text)`         | Count the number of digits                  | `count_digits("Hello 123!")` → `3`                            |
| `mask_part(text, visible=4)` | Hide part of text behind asterisks          | `mask_part("1234567890", 4)` → `"1234 ******"`                |
| `pluralize(word, count)`     | Get the singular or plural form             | `pluralize("cat", 3)` → `"cats"`                              |
| `extract_hashtags(text)`     | Extract hashtags without the # symbol       | `extract_hashtags("#python rocks")` → `["python"]`            |
| `word_frequency(text)`       | Count how often each word appears           | `word_frequency("the cat and the dog")` → `{"the": 2, ...}`   |

</details>

### 🔄 Easy Converter

<details>
<summary>Click to expand — unit conversions without memorizing formulas</summary>

<br>

**Time**

| Function                       | Example      |
|--------------------------------|--------------|
| `seconds_to_hh_mm_ss(3665)`    | `"01:01:05"` |
| `hh_mm_ss_to_seconds(1, 1, 1)` | `3661`       |

**Distance & Length**

| Function                 | Example  |
|--------------------------|----------|
| `km_to_mile(100)`        | `62.13`  |
| `miles_to_km(100)`       | `160.93` |
| `meters_to_feet(100)`    | `328.08` |
| `feet_to_meters(328.08)` | `100.0`  |
| `cm_to_inches(100)`      | `39.37`  |
| `inches_to_cm(39.37)`    | `100.0`  |

**Weight**

| Function           | Example |
|--------------------|---------|
| `kg_to_lb(5)`      | `11.02` |
| `lb_to_kg(110.23)` | `50.0`  |

**Temperature**

| Function                     | Example |
|------------------------------|---------|
| `celsius_to_fahrenheit(25)`  | `77.0`  |
| `fahrenheit_to_celsius(104)` | `40.0`  |

**Volume**

| Function                           | Example |
|------------------------------------|---------|
| `fluid_oz_to_ml(1, standard='us')` | `29.6`  |
| `fluid_oz_to_ml(1, standard='uk')` | `28.4`  |
| `ml_to_fluid_oz(1, standard='us')` | `0.03`  |
| `ml_to_fluid_oz(1, standard='uk')` | `0.04`  |

**Area**

| Function                       | Example  |
|--------------------------------|----------|
| `sq_meters_to_sq_feet(10)`     | `107.64` |
| `sq_feet_to_sq_meters(107.64)` | `10.0`   |

**Speed**

| Function               | Example |
|------------------------|---------|
| `mph_to_kph(0.621371)` | `1.0`   |
| `kph_to_mph(1.60934)`  | `1.0`   |

</details>

### ✅ Easy Validator

<details>
<summary>Click to expand — input validation without regex memorization</summary>

<br>

| Function                  | What it checks                                      | Example                                      |
|---------------------------|-----------------------------------------------------|----------------------------------------------|
| `is_valid_email(str)`     | Valid email format                                  | `is_valid_email("hello@world.com")` → `True` |
| `is_valid_username(str)`  | Letters, numbers, and underscores only              | `is_valid_username("user_name")` → `True`    |
| `is_valid_url(str)`       | URLs with http, https, or www                       | `is_valid_url("www.google.com")` → `True`    |
| `is_valid_zipcode(int)`   | 5-digit US zip code                                 | `is_valid_zipcode(12345)` → `True`           |
| `is_password_secure(str)` | 8+ chars, upper, lower, digits, special, no repeats | `is_password_secure("1andkrf!AG5")` → `True` |

</details>

### 🌐 Easy Web

<details>
<summary>Click to expand — web scraping and checks without the requests/BS4 boilerplate</summary>

<br>

| Function                    | What it does                                     | Example                                                   |
|-----------------------------|--------------------------------------------------|-----------------------------------------------------------|
| `is_page_up(url)`           | Check if a site returns 200                      | `is_page_up("https://github.com")` → `True`               |
| `get_page_title(url)`       | Get the page title                               | `get_page_title("https://github.com")` → `"GitHub · ..."` |
| `get_page_content(url)`     | Get prettified HTML                              | `get_page_content("https://google.com")`                  |
| `count_links(url)`          | Count links on a page                            | `count_links("https://github.com")` → `144`               |
| `get_link_list(url)`        | Get all links as a list                          | `get_link_list("https://github.com")` → `[...]`           |
| `count_tags(url, tag)`      | Count tags of a given type (e.g. `'a'`, `'img'`) | `count_tags("https://github.com", "img")` → `12`          |
| `get_tag_list(url, tag)`    | Get useful info from each matching tag           | `get_tag_list("https://github.com", "img")` → `[...]`     |
| `print_allowed_tags()`      | Print the supported tag → attribute map          | `print_allowed_tags()` → `{'a': 'href', 'img': 'src'}`    |
| `get_meta_description(url)` | Get all meta tag contents                        | `get_meta_description("https://github.com")` → `[...]`    |
| `get_all_headers(url)`      | Get text from all `<header>` tags                | `get_all_headers("https://github.com")` → `[...]`         |

</details>

### 🎨 Easy Colors

<details>
<summary>Click to expand — hex/RGB/HSL color conversions without memorizing the formulas</summary>

<br>

| Function                                   | What it does                                                          | Example                                                    |
|-----------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------|
| `is_valid_hex(hex_code)`                       | Checks whether a string is a valid hex color code                        | `is_valid_hex("#FFFFFF")` → `True`                               |
| `hex_to_rgb(hex_code)`                         | Converts a hex color code to an (R, G, B) tuple                          | `hex_to_rgb("#FFFFFF")` → `(255, 255, 255)`                      |
| `rgb_to_hex(r, g, b)`                          | Converts (R, G, B) values to a hex color string                          | `rgb_to_hex(255, 255, 255)` → `"#FFFFFF"`                        |
| `rgb_to_hsl(r, g, b)`                          | Converts (R, G, B) values to an (H, S, L) tuple                          | `rgb_to_hsl(255, 0, 0)` → `(0.0, 100.0, 50.0)`                   |
| `hsl_to_rgb(h, s, lightness)`                  | Converts an (H, S, L) color to an (R, G, B) tuple                        | `hsl_to_rgb(120, 100, 50)` → `(0, 255, 0)`                       |
| `random_hex_color()`                           | Returns a random valid hex color string                                  | `random_hex_color()` → e.g. `"#A1B2C3"`                          |
| `is_light_color(hex_code)`                     | Returns whether a hex color is "light" based on perceived luminance      | `is_light_color("#FFFFFF")` → `True`                             |
| `hex_to_rgba(hex_code, alpha)`                 | Converts a hex color and alpha value into an (R, G, B, A) tuple          | `hex_to_rgba("#FF0000", 0.5)` → `(255, 0, 0, 0.5)`               |
| `contrast_ratio(hex1, hex2)`                   | Calculates WCAG contrast ratio between two hex colors                    | `contrast_ratio("#000000", "#FFFFFF")` → `21.0`                  |

</details>

### 🔄 Easy Flow

<details>
<summary>Click to expand — running scripts, timing, and retries without the boilerplate</summary>

<br>

| Function                                   | What it does                                                             | Example                                          |
|---------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------|
| `run_py_file(filename)`                      | Runs a `.py` file as `__main__`, raising `EasyFlowError` on failure          | `run_py_file("script.py")`                           |
| `run_py_file_safe(filename)`                 | Same as `run_py_file`, but returns `(success, error)` instead of raising     | `success, error = run_py_file_safe("script.py")`      |
| `time_function_call(function, args=None)`    | Runs a function once and returns how long it took, in seconds                | `time_function_call(add, [2, 3])` → `0.000002`        |
| `time_it`                                    | Decorator that times a function and prints how long it took                  | `@time_it` above a function definition               |
| `retry(func, attempts=3, delay=1)`           | Calls a function, retrying it if it fails, with a pause between attempts     | `retry(flaky_api, attempts=5, delay=2)`               |

</details>

### 📄 Easy JSON

<details>
<summary>Click to expand — JSON file handling without the boilerplate</summary>

<br>

| Function                     | What it does                                 | Example                                                             |
|------------------------------|----------------------------------------------|---------------------------------------------------------------------|
| `open_json(path)`            | Read a JSON file into a dict                 | `open_json("config.json")`                                          |
| `save_json_data(path, dict)` | Save a dict to a new JSON file               | `save_json_data("config.json", {"name": "Sara"})`                   |
| `update_json(path, dict)`    | Merge new data into an existing JSON file    | `update_json("config.json", {"name": "Sara"})`                      |
| `pretty_json(data=dict)`     | Pretty-print a dict as indented JSON         | `pretty_json(data={"name": "Sara"})`                                |
| `pretty_json(filepath=path)` | Pretty-print a JSON file's contents          | `pretty_json(filepath="config.json")`                               |
| `is_json_file(path)`         | Check if a file exists and is .json          | `is_json_file("config.json")` → `True`                              |
| `is_nested_json(data=dict)`  | Check if a dict has any nested dicts/lists   | `is_nested_json(data={"a": 1, "b": {"c": 2}})` → `True`             |
| `flatten_json(data=dict)`    | Flatten a nested dict into single-level keys | `flatten_json(data={"a": 1, "b": {"c": 2}})` → `{"a": 1, "b-c": 2}` |

</details>

### 🔍 Easy Regex
 
<details>
<summary>Click to expand — pull common patterns out of text without writing regex</summary>

<br>

| Function                         | What it does                                                                   | Example                                                                            |
|----------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| `extract_emails(text)`           | Find all email addresses in text                                               | `extract_emails("Contact hello@example.com")` → `['hello@example.com']`            |
| `extract_urls(text)`             | Find all URLs in text                                                          | `extract_urls("Visit www.example.com")` → `['www.example.com']`                    |
| `extract_number_sequences(text)` | Find number sequences joined by `-`, `_`, `:`, or `.` (dates, times, IPs, IDs) | `extract_number_sequences("IP 192.168.1.1 at 14:32")` → `['192.168.1.1', '14:32']` |
| `extract_numbers(text)`          | Find all standalone digit sequences                                            | `extract_numbers("I have 3 cats and 12 fish")` → `['3', '12']`                     |
 
</details>

### ⚡ Easy Async

<details>
<summary>Click to expand — run multiple functions at the same time without touching ThreadPoolExecutor directly</summary>

<br>

| Function                                               | What it does                                                          | Example                                                                                     |
|--------------------------------------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `run_at_the_same_time_no_params(functions)`            | Runs multiple functions at the same time                              | `run_at_the_same_time_no_params([add, sub])` → `[('add', 2), ('sub', 2)]`                   |
| `run_at_the_same_time_with_params(functions_and_args)` | Runs multiple functions at the same time, each with its own arguments | `run_at_the_same_time_with_params([(add, 1, 1), (sub, 4, 2)])` → `[('add', 2), ('sub', 2)]` |

</details>

### 🔑 Easy Dict

<details>
<summary>Click to expand — dictionary operations without the boilerplate</summary>

<br>

| Function                             | What it does                                                              | Example                                                                                 |
|--------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| `merge_dicts(dict_a, dict_b)`        | Combines two dictionaries, dict_b wins on shared keys                     | `merge_dicts({"a": 1}, {"b": 2})` → `{"a": 1, "b": 2}`                                   |
| `lists_to_dict(keys, values)`        | Combines two lists into a dictionary, pairing them by position            | `lists_to_dict(["name", "age"], ["Ana", 25])` → `{"name": "Ana", "age": 25}`             |
| `invert_dict(dictionary)`            | Returns a new dictionary with keys and values swapped                     | `invert_dict({"a": 1, "b": 2})` → `{1: "a", 2: "b"}`                                     |
| `get_nested_value(dictionary, path)` | Gets a nested value using a dot-separated path, with a default fallback   | `get_nested_value({"user": {"name": "Ana"}}, "user.name")` → `"Ana"`                     |
| `sort_dict_by_key(dictionary)`       | Returns a new dictionary with keys sorted alphabetically                  | `sort_dict_by_key({"b": 2, "a": 1})` → `{"a": 1, "b": 2}`                                |
| `sort_dict_by_value(dictionary)`     | Returns a new dictionary with values sorted from smallest to largest      | `sort_dict_by_value({"a": 2, "b": 1})` → `{"b": 1, "a": 2}`                              |
| `rename_key(dictionary, old, new)`   | Returns a copy of the dictionary with one key renamed                     | `rename_key({"name": "Ana"}, "name", "username")` → `{"username": "Ana"}`                |
| `find_keys(needle, dictionary)`      | Returns every key whose value matches the given needle                    | `find_keys(1, {"a": 1, "b": 2, "c": 1})` → `["a", "c"]`                                  |
| `count_values(dictionary)`           | Counts how many times each value appears in the dictionary                | `count_values({"a": 1, "b": 2, "c": 1})` → `{1: 2, 2: 1}`                                |
| `most_common_value(dictionary)`      | Returns the value that appears most often in the dictionary               | `most_common_value({"a": 1, "b": 2, "c": 1})` → `1`                                      |

</details>

### 🖼️ Easy Images

<details>
<summary>Click to expand — resize, convert, rotate, and inspect images without wrangling Pillow directly</summary>

<br>

| Function                                                 | What it does                                                   | Example                                                                                            |
|----------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `resize_image("photo.jpg", "photo_small.jpg", 320, 240)` | Resize an image to given dimensions and save it                | Saves a 320×240 version of `photo.jpg` as `photo_small.jpg`                                        |
| `convert_image("photo.png", "photo.jpg")`                | Convert an image to a different format based on file extension | Saves `photo.png` as a JPEG at `photo.jpg`                                                         |
| `rotate_image("photo.jpg", "photo_rotated.jpg", 90)`     | Rotate an image by an angle (counter-clockwise) and save it    | Saves `photo.jpg` rotated 90° as `photo_rotated.jpg`                                               |
| `get_image_info("photo.jpg")`                            | Get basic info about an image                                  | `get_image_info("photo.jpg")` → `{"width": 1920, "height": 1080, "format": "JPEG", "mode": "RGB"}` |

</details>


### 🧮 Easy Math

<details>
<summary>Click to expand — math helpers without re-deriving the formulas</summary>

<br>

| Function                                   | What it does                                                      | Example                                                                   |
|--------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------|
| `get_least_common_multiple(a, b)`                                | Returns the least common multiple of two integers                 | `get_least_common_multiple(4, 6)` → `12`                                                         |
| `factorial(n)`                             | Returns the factorial of a whole number                           | `factorial(5)` → `120`                                                     |
| `fibonacci(count)`                         | Returns the first `count` Fibonacci numbers                       | `fibonacci(5)` → `[0, 1, 1, 2, 3]`                                         |
| `prime_factorization(n)`                         | Returns the prime factors of a number, including repeats          | `prime_factorization(12)` → `[2, 2, 3]`                                          |
| `sum_of_digits(n)`                         | Returns the sum of the digits of an integer                       | `sum_of_digits(1234)` → `10`                                               |
| `divisors(n)`                              | Returns every positive integer that divides n evenly              | `divisors(12)` → `[1, 2, 3, 4, 6, 12]`                                     |

</details>
  
### 📊 Easy Stats

<details>
<summary>Click to expand — statistics operations without memorizing the formulas</summary>

<br>

| Function                                   | What it does                                                       | Example                                                                                     |
|--------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `median(nums)`                             | Returns the middle value of a list of numbers                      | `median([4, 1, 9, 2])` → `3.0`                                                              |
| `mode(nums)`                               | Returns the number that appears most often                         | `mode([2, 1, 2, 3])` → `2`                                                                  |
| `data_range(nums)`                         | Returns the difference between the largest and smallest numbers    | `data_range([4, 1, 8, 2])` → `7`                                                            |
| `variance(nums)`                           | Returns how spread out the numbers are, as sample variance         | `variance([1, 2, 3])` → `1.0`                                                               |
| `standard_deviation(nums)`                 | Returns how far numbers typically sit from the average             | `standard_deviation([1, 2, 3])` → `1.0`                                                     |
| `percentile(nums, percent)`                | Returns the value below which the given percent of numbers fall    | `percentile([1, 2, 3, 4], 75)` → `3`                                                        |

</details>

### 📑 Easy CSV

<details>
<summary>Click to expand — CSV reading and writing without the <code>csv</code> module boilerplate</summary>

<br>

| Function                                                    | What it does                                            | Example                                                                     |
|--------------------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------|
| `read_csv_to_list("people.csv")`                              | Reads a CSV file into a list of dicts (or lists)          | `read_csv_to_list("people.csv")` → `[{'Name': 'Alice', 'Age': '24'}]`        |
| `write_csv_from_list("people.csv", data)`                     | Writes a list of dicts or lists to a CSV file             | `write_csv_from_list("people.csv", [{"Name": "Alice", "Age": "24"}])`        |
| `get_csv_columns("people.csv")`                                | Returns the column headers of a CSV file                  | `get_csv_columns("people.csv")` → `['Name', 'Age']`                          |
| `filter_csv_rows("people.csv", "Name", "Alice")`               | Returns rows where a column matches a given value          | `filter_csv_rows("people.csv", "Name", "Alice")` → `[{'Name': 'Alice', 'Age': '24'}]` |

</details>

### 🎮 Easy Game

<details>
<summary>Click to expand — pygame setup without the boilerplate</summary>

<br>

| Function                                        | What it does                                                        | Example                                                        |
|--------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------|
| `basic_game_setup(800, 600, "My Game")`           | Sets up a pygame window and clock in one call (init, display, caption, clock) | `screen, clock = basic_game_setup(800, 600, "My Game")`           |

</details>

## 🤝 Contributing

I would love to have your help in making Python simpler for everyone!

Contributions of all sizes are welcome:

- Fix documentation
- Improve existing modules
- Suggest new features
- Add new functionality
- Improve examples

Please check [CONTRIBUTING.md](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md) before submitting changes.

Every contribution helps make py-simple-wrap better for beginners and developers.

---

## 🤝 Contributors

A huge thank you to these wonderful people for helping make Python simpler for everyone!

#### Emoji Key:
- 💻 = Code
- 📖 = Docs
- 🐛 = Bug Reports
- 🧪 = Tests
- 🚇 = Infrastructure
- 🛡️ = Maintainer
- 👑 = Original Author
- 🚀 = Project Management
- ✋ = Collaborators

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sara-czasak"><img src="https://avatars.githubusercontent.com/u/217280993?v=4?s=100" width="100px;" alt="Sara Czasak"/><br /><sub><b>Sara Czasak</b></sub></a><br /><a href="https://github.com/sara-czasak" title="Maintainer">🛡️</a> <a href="https://github.com/sara-czasak" title="Project Management">🚀</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=sara-czasak" title="Code">💻</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=sara-czasak" title="Docs">📖</a> <a href="https://github.com/sara-czasak" title="Original Author">👑</a> <a href="https://github.com/sara-czasak" title="Collaborators">✋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jagjitkaur0000"><img src="https://avatars.githubusercontent.com/u/226679809?v=4?s=100" width="100px;" alt="jagjitkaur0000"/><br /><sub><b>jagjitkaur0000</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=jagjitkaur0000" title="Tests">🧪</a> <a href="https://github.com/jagjitkaur0000" title="Collaborators">✋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/atiqur-rahman-pro"><img src="https://avatars.githubusercontent.com/u/264598807?v=4?s=100" width="100px;" alt="atiqur rahman"/><br /><sub><b>atiqur rahman</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=atiqur-rahman-pro" title="Tests">🧪</a> <a href="https://github.com/atiqur-rahman-pro" title="Collaborators">✋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/gaoharimran29-glitch"><img src="https://avatars.githubusercontent.com/u/225884102?v=4?s=100" width="100px;" alt="Gaohar Imran"/><br /><sub><b>Gaohar Imran</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=gaoharimran29-glitch" title="Tests">🧪</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=gaoharimran29-glitch" title="Code">💻</a> <a href="https://github.com/gaoharimran29-glitch" title="Collaborators">✋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Onion0121"><img src="https://avatars.githubusercontent.com/u/246456340?v=4?s=100" width="100px;" alt="Yassin Azzouzi"/><br /><sub><b>Yassin Azzouzi</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=Onion0121" title="Docs">📖</a> <a href="https://github.com/Onion0121" title="Collaborators">✋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ghostfix-pm"><img src="https://avatars.githubusercontent.com/u/307249429?v=4?s=100" width="100px;" alt="ghostfix-pm"/><br /><sub><b>ghostfix-pm</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=ghostfix-pm" title="Infrastructure">🚇</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=ghostfix-pm" title="Tests">🧪</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=ghostfix-pm" title="Code">💻</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=ghostfix-pm" title="Docs">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sol4nki"><img src="https://avatars.githubusercontent.com/u/75659510?v=4?s=100" width="100px;" alt="Pranjal Solanki"/><br /><sub><b>Pranjal Solanki</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=sol4nki" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/shivams786"><img src="https://avatars.githubusercontent.com/u/143723566?v=4?s=100" width="100px;" alt="Shivam Singh"/><br /><sub><b>Shivam Singh</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=shivams786" title="Docs">📖</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=shivams786" title="Tests">🧪</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=shivams786" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/leepCh"><img src="https://avatars.githubusercontent.com/u/195529175?v=4?s=100" width="100px;" alt="Challa Leela Prasad"/><br /><sub><b>Challa Leela Prasad</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=leepCh" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/HeaTTap"><img src="https://avatars.githubusercontent.com/u/83951176?v=4?s=100" width="100px;" alt="HeaTTap"/><br /><sub><b>HeaTTap</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=HeaTTap" title="Docs">📖</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=HeaTTap" title="Tests">🧪</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=HeaTTap" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/averyquinnhq"><img src="https://avatars.githubusercontent.com/u/309920345?v=4?s=100" width="100px;" alt="Avery Quinn"/><br /><sub><b>Avery Quinn</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=averyquinnhq" title="Tests">🧪</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mmaxjr"><img src="https://avatars.githubusercontent.com/u/9955641?v=4?s=100" width="100px;" alt="Marcos Max"/><br /><sub><b>Marcos Max</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=mmaxjr" title="Docs">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/matheusfrta"><img src="https://avatars.githubusercontent.com/u/217668693?v=4?s=100" width="100px;" alt="Matheus"/><br /><sub><b>Matheus</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=matheusfrta" title="Tests">🧪</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Mlandvo"><img src="https://avatars.githubusercontent.com/u/39243759?v=4?s=100" width="100px;" alt="Mlandvo Maphalala"/><br /><sub><b>Mlandvo Maphalala</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=Mlandvo" title="Tests">🧪</a> <a href="https://github.com/sara-czasak/py_simple/issues?q=author%3AMlandvo" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/qotique"><img src="https://github.com/qotique.png?s=100" width="100px;" alt="qotique"/><br /><sub><b>qotique</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=qotique" title="Docs">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/AureSerua"><img src="https://github.com/AureSerua.png?s=100" width="100px;" alt="AureSerua"/><br /><sub><b>AureSerua</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=AureSerua" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SemTiOne"><img src="https://github.com/SemTiOne.png?s=100" width="100px;" alt="Dane Parin"/><br /><sub><b>Dane Parin</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=SemTiOne" title="Code">💻</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=SemTiOne" title="Tests">🧪</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vjymisal0"><img src="https://github.com/vjymisal0.png?s=100" width="100px;" alt="Vijay Misal"/><br /><sub><b>Vijay Misal</b></sub></a><br /><a href="https://github.com/sara-czasak/py_simple/commits?author=vjymisal0" title="Code">💻</a> <a href="https://github.com/sara-czasak/py_simple/commits?author=vjymisal0" title="Tests">🧪</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

---

## ⚖️ License

This project is licensed under the MIT License.

You are free to use, modify, and distribute it.

See the [LICENSE.md](LICENSE.md) file for the full legal text.
