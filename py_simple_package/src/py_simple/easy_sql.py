"""
Beginner friendly helpers for handling databases.
"""

import sqlite3


class EasySqlError(Exception):
    """
    Custom exception for py_simple SQL helpers.

    Raised when a database operation fails — for example, when the
    connection to the database file cannot be established.

    Args:
        message (str): Description of what went wrong.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def open_db(db_filepath: str) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Opens a connection to an SQLite database file. Creates the file if it
    doesn't exist yet; opens it as-is if it does.

    Args:
        db_filepath (str): Filepath to the database.

    Returns:
        connection (sqlite3.Connection): Open connection to the database.
        cursor (sqlite3.Cursor): Cursor for executing SQL statements.

    Raises:
        EasySqlError: If the connection to the database fails.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import open_db

            connection, cursor = open_db('mydb.db')
            ```

        === "The Traditional Way"
            ```python
            import sqlite3

            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            ```
    """
    try:
        conn = sqlite3.connect(db_filepath)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.OperationalError as e:
        raise EasySqlError(f"\n\nERROR: {e}") from None


def run_query(cursor: sqlite3.Cursor , query_type: str, params: tuple) -> tuple | None:
    pass