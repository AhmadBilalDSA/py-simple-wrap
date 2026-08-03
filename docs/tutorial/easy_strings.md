# Easy Strings

Working with text is something you'll do in almost every Python project. Whether you're cleaning user input, creating filenames, or preparing text for URLs, `easy_strings` provides simple helpers that keep your code easy to read.

## A small real-world example

Imagine you're collecting article titles from users. Before saving them, you want to:

- remove extra spaces,
- create a `snake_case` filename,
- count how many words the title contains.

```python
from py_simple import remove_extra_spaces, to_snake_case, count_words

title = "   My   First    Python Project!   "

clean_title = remove_extra_spaces(title)
filename = to_snake_case(clean_title)
words = count_words(clean_title)

print(clean_title)
# My First Python Project!

print(filename)
# my_first_python_project

print(words)
# 4
```

## What happened?

`remove_extra_spaces()` removes leading, trailing, and repeated spaces from the text.

`to_snake_case()` converts the cleaned text into `snake_case`, making it useful for filenames, variables, or URLs.

`count_words()` counts the number of words in the cleaned text without needing any extra logic.

## Why use these helpers?

Instead of combining multiple string methods and regular expressions every time, you can write cleaner and more readable code:

```python
clean_title = remove_extra_spaces(title)
filename = to_snake_case(clean_title)
words = count_words(clean_title)
```

These helpers keep your code simple, readable, and beginner-friendly.