# Easy Random

Choosing random values is useful for games, raffles, quizzes, and small experiments. The `easy_random` module wraps Python's `random` module with beginner-friendly helpers for common tasks.

## A small real-world example

Imagine you're drawing a winner from a short list of raffle entries. You can shuffle a copy of the entries and choose the first name without changing the original list.

```python
import random
from py_simple import shuffle_list, pick_random_item

random.seed(7)  # Makes this example repeatable while you learn.
entries = ["Aiko", "Ben", "Chika"]
shuffled_entries = shuffle_list(entries)
winner = pick_random_item(shuffled_entries)

print(shuffled_entries)
print(winner)
```

Example output:

```text
['Chika', 'Aiko', 'Ben']
Aiko
```

## What happened?

`shuffle_list()` returned a new list with the entries in random order, leaving `entries` unchanged.

`pick_random_item()` selected one item from the shuffled list. The module also includes `roll_dice()` for a random number from 1 to a chosen number of sides, `flip_coin()` for `Heads` or `Tails`, and `random_int()` for an integer between two inclusive limits.

## Why use these helpers?

Without these helpers, you would need to remember which `random` function fits each task and write the surrounding list-copying or validation code yourself. These small wrappers keep everyday random choices readable, while still letting Python handle the randomness.
