# Easy Converter

Converting between different units is something you'll encounter in many Python projects. Whether you're working with time, distance, temperature, weight, or speed, `easy_converter` provides beginner-friendly helpers that make common conversions simple and easy to read. :contentReference[oaicite:0]{index=0}

## A small real-world example

Imagine you're building a fitness application. Before displaying the user's information, you want to convert their weight from kilograms to pounds, their running distance from kilometers to miles, and today's temperature from Celsius to Fahrenheit.

```python
from py_simple import kg_to_lb, km_to_mile, celsius_to_fahrenheit

weight = kg_to_lb(75)
distance = km_to_mile(10)
temperature = celsius_to_fahrenheit(22)

print(weight)
print(distance)
print(temperature)
```

Example output:

```text
165.35
6.21
71.6
```

## What happened?

`kg_to_lb()` converts kilograms into pounds.

`km_to_mile()` converts kilometers into miles.

`celsius_to_fahrenheit()` converts temperatures from Celsius to Fahrenheit.

The module also includes many other conversion helpers for time, temperature, length, weight, area, volume, and speed, so you don't need to remember conversion formulas. :contentReference[oaicite:1]{index=1}

## Why use these helpers?

Instead of writing conversion formulas every time, you can simply write:

```python
weight = kg_to_lb(75)
distance = km_to_mile(10)
temperature = celsius_to_fahrenheit(22)
```

These helpers keep unit conversions simple, readable, and beginner-friendly while providing a wide range of commonly used conversions.