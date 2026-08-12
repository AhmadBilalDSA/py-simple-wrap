# Easy Math

Working with numbers is an essential part of programming, from simple calculations to data analysis and cryptography. `easy_math` provides beginner-friendly helpers that make some common math tasks simple and easy to read.

## A small real-world example

Imagine you're building a simple lottery ticket generator for a charity raffle. Each ticket gets a number from the Fibonacci sequence. The organisers will later use two properties of the ticket number to decide the prize: the sum of its digits and its prime factors.

```python
from py_simple import fibonacci, sum_of_digits, prime_factorization

ticket_numbers = fibonacci(10)
winning_ticket = ticket_numbers[-1]
digit_sum = sum_of_digits(winning_ticket)
factors = prime_factorization(winning_ticket)

print(f"Winning ticket number: {winning_ticket}")
print(f"Sum of digits: {digit_sum}")
print(f"Prime factors: {factors}")
```

Example output:

```text
Winning ticket number: 34
Sum of digits: 7
Prime factors: [2, 17]
```

## What happened?

`fibonacci()` returns the first N Fibonacci numbers as a list.

`sum_of_digits()` returns the sum of all digits in a number.

`prime_factorization()` returns the prime factors of a number, including repeats.

## Why use these helpers?

Instead of writing loops to generate sequences, manually summing digits, or implementing factorisation code by yourself, you can use a few simple functions:

```python
ticket_numbers = fibonacci(10)
winning_ticket = ticket_numbers[-1]
digit_sum = sum_of_digits(winning_ticket)
factors = prime_factorization(winning_ticket)
```

This makes your code simpler, more readable, and approachable for beginners.