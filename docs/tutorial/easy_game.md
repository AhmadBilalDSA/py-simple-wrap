# Easy Game

Working with games in Python often means setting up Pygame, creating a game window, handling events, and checking mouse input. The `easy_game` module provides simple helpers that remove some of this boilerplate and make getting started with Pygame easier.

## A small real-world example

Imagine you're creating a simple game where you need to open a window, keep track of the game clock, detect when the player closes the window, and check whether the player is pressing the mouse buttons.

```python
from py_simple import (
    basic_game_setup,
    check_if_quit,
    get_mouse_position,
    is_left_mouse_button_clicked,
)

screen, clock = basic_game_setup(800, 600, "My Game")

running = True

while running:
    if check_if_quit():
        running = False

    x, y = get_mouse_position()

    if is_left_mouse_button_clicked():
        print(f"Mouse clicked at: {x}, {y}")

    clock.tick(60)
```

## What happened?

`basic_game_setup()` initializes Pygame, creates the game window, sets its title, and creates a clock for controlling the game loop.

`check_if_quit()` checks the Pygame event queue and returns `True` when the player closes the game window.

`get_mouse_position()` returns the current `(x, y)` position of the mouse cursor.

`is_left_mouse_button_clicked()` checks whether the left mouse button is currently being held down.

The module also provides helpers for checking the middle and right mouse buttons:

```python
from py_simple import (
    is_middle_mouse_button_clicked,
    is_right_mouse_button_clicked,
)

if is_middle_mouse_button_clicked():
    print("Middle mouse button!")

if is_right_mouse_button_clicked():
    print("Right mouse button!")
```

## Why use these helpers?

Instead of repeatedly writing Pygame initialization, event handling, and mouse input code, you can simply use:

```python
screen, clock = basic_game_setup(800, 600, "My Game")

while True:
    if check_if_quit():
        break

    x, y = get_mouse_position()

    if is_left_mouse_button_clicked():
        print(x, y)

    clock.tick(60)
```

These helpers keep common Pygame tasks simple, readable, and beginner-friendly while letting you focus on building the actual game.