# Building a Mystery Number Quest Game with Easy Random and Easy Game

Combine **Easy Random** and **Easy Game** to build an interactive, beginner-friendly number guessing adventure in just a few lines of Python!

## A small real-world example

Imagine you want to quickly spin up a fun command-line game where a player tries to guess a secret number within a limited number of tries, complete with colorful prompts and automated score tracking.

```python
from py_simple import get_random_integer, start_game_loop

def play_quest():
    secret_number = get_random_integer(1, 50)
    print("Welcome to the Mystery Number Quest! Guess a number between 1 and 50.")
    
    # Run a simple game loop with 5 attempts
    success = start_game_loop(secret_number, max_attempts=5)
    if success:
        print("Congratulations, adventurer! You found the treasure!")
    else:
        print("Oh no! You ran out of attempts. Better luck next time!")

if __name__ == "__main__":
    play_quest()