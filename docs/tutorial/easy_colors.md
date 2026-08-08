# Easy Colors

Working with colors is common when building websites, user interfaces, data visualizations, or graphics. Whether you're converting between color formats, validating user input, or checking color accessibility, `easy_colors` provides beginner-friendly helpers that make color manipulation simple and easy to read. :contentReference[oaicite:0]{index=0}

## A small real-world example

Imagine you're creating a website where users can choose a theme color. Before saving it, you want to verify that the color is valid, convert it to RGB, and determine whether it's considered a light color.

```python
from py_simple import is_valid_hex, hex_to_rgb, is_light_color

color = "#4CAF50"

if is_valid_hex(color):
    print(hex_to_rgb(color))
    print(is_light_color(color))
else:
    print("Invalid color.")
```

Example output:

```text
(76, 175, 80)
True
```

## What happened?

`is_valid_hex()` checks whether the input is a valid hexadecimal color code.

`hex_to_rgb()` converts the hexadecimal color into an `(R, G, B)` tuple.

`is_light_color()` calculates the perceived luminance of the color and determines whether it should be considered light, making it useful for choosing readable text colors. :contentReference[oaicite:1]{index=1}

## Why use these helpers?

Instead of writing regular expressions, manually converting color formats, or implementing luminance calculations yourself, you can simply write:

```python
if is_valid_hex(color):
    rgb = hex_to_rgb(color)
    light = is_light_color(color)
```

These helpers keep color manipulation simple, readable, and beginner-friendly while providing useful tools for validation, conversion, accessibility, and working with RGB, HSL, RGBA, and hexadecimal colors.