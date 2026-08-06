import pygame


class EasyGameError(Exception):
    """
        Raised when a pygame window/game can't be set up.

        Wraps whatever pygame raises internally (bad dimensions, display
        driver issues, etc.) so py_simple functions can fail with one
        consistent, easy-to-read exception instead of a random builtin
        or pygame-specific one.

        Args:
            message (str): Human-readable description of what went wrong.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def basic_game_setup(width: int, height: int, title: str ="My Game") -> tuple:
    """
    Sets up a pygame window and clock in one call, handling the
    pygame.init(), display, caption, and clock boilerplate every
    pygame project needs before the game loop can start.

    Args:
        width (int): Width of the game window, in pixels.
        height (int): Height of the game window, in pixels.
        title (str, optional): Text shown in the window's title bar.
            Defaults to `"My Game"`.

    Returns:
        tuple: `(screen, clock)`, where `screen` is the pygame
            `Surface` returned by `pygame.display.set_mode()` and
            `clock` is a `pygame.time.Clock` instance.

    Raises:
        EasyGameError: If pygame fails to initialize or set up the
            window (e.g. invalid width/height, display driver issue).

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import basic_game_setup

            screen, clock = basic_game_setup(800, 600, "My Game")
            ```

        === "The Traditional Way"
            ```python
            import pygame

            pygame.init()
            screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("My Game")
            clock = pygame.time.Clock()
            ```
    """
    try:
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        clock = pygame.time.Clock()
        return screen, clock
    except Exception as e:
        raise EasyGameError(f"\n\n\nERROR: {e}") from None


