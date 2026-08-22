"""
easy_random is built to simplify common random choices, numbers, and shuffling.
"""

import random
from typing import Any, Sequence, List


def roll_dice(sides: int = 6) -> int:
    """
    Simulates rolling a die with a given number of sides (default is 6).

    Args:
        sides (int): Number of sides on the die. Defaults to 6.

    Returns:
        int: A random integer between 1 and sides inclusive.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import roll_dice

            result = roll_dice(6)  # -> e.g. 4
            ```

        === "The Traditional Way"
            ```python
            import random

            result = random.randint(1, 6)
            ```
    """
    if sides < 1:
        raise ValueError("Dice must have at least 1 side.")
    return random.randint(1, sides)


def flip_coin() -> str:
    """
    Simulates a coin toss, returning 'Heads' or 'Tails'.

    Returns:
        str: 'Heads' or 'Tails'.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import flip_coin

            result = flip_coin()  # -> 'Heads'
            ```

        === "The Traditional Way"
            ```python
            import random

            result = random.choice(["Heads", "Tails"])
            ```
    """
    return random.choice(["Heads", "Tails"])


def pick_random_item(items: Sequence[Any]) -> Any:
    """
    Picks a single random element from a list or tuple.

    Args:
        items (Sequence[Any]): The collection to pick from.

    Returns:
        Any: A randomly chosen element from the sequence.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import pick_random_item

            fruit = pick_random_item(["apple", "banana", "cherry"])  # -> 'banana'
            ```

        === "The Traditional Way"
            ```python
            import random

            fruit = random.choice(["apple", "banana", "cherry"])
            ```
    """
    if not items:
        raise ValueError("Cannot pick an item from an empty sequence.")
    return random.choice(items)


def shuffle_list(items: Sequence[Any]) -> List[Any]:
    """
    Returns a new list with the items shuffled in random order.

    Args:
        items (Sequence[Any]): The items to shuffle.

    Returns:
        List[Any]: A new shuffled copy of the list.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import shuffle_list

            shuffled = shuffle_list([1, 2, 3, 4, 5])  # -> e.g. [3, 1, 5, 2, 4]
            ```

        === "The Traditional Way"
            ```python
            import random

            my_list = [1, 2, 3, 4, 5]
            shuffled = list(my_list)
            random.shuffle(shuffled)
            ```
    """
    result = list(items)
    random.shuffle(result)
    return result


def random_int(start: int, end: int) -> int:
    """
    Generates a random integer between start and end (inclusive).

    Args:
        start (int): The lower bound.
        end (int): The upper bound.

    Returns:
        int: A random integer within [start, end].

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import random_int

            num = random_int(10, 20)  # -> e.g. 17
            ```

        === "The Traditional Way"
            ```python
            import random

            num = random.randint(10, 20)
            ```
    """
    if start > end:
        raise ValueError("start cannot be greater than end.")
    return random.randint(start, end)