"""
Beginner friendly helpers for handling databases.
"""

import sqlite3
import re


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


def _check_if_valid(to_check: str) -> bool | None:
    forbidden = ['union', 'union all', 'select', 'join', 'insert',
                 'update', 'delete', 'drop', 'alter', 'create', 'truncate',
                 'replace', 'attach', 'detach', 'pragma', 'vacuum',
                 'sqlite_master', 'sqlite_version', 'sqlite_temp_master',
                 'load_extension', 'randomblob', 'zeroblob', 'glob',
                 'like']

    if not isinstance(to_check, str):
        return False

    pieces = [p.strip() for p in to_check.split(",")]
    for i in forbidden:
        if i in to_check.lower():
            return False
    if to_check == "*":
        return True
    return all(
        re.fullmatch(r"[0-9A-Za-z_]+", p) for p in pieces)


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


def run_select(connection: sqlite3.Connection, cursor: sqlite3.Cursor ,
               table_name: str, to_select: str):
    if _check_if_valid(table_name) and _check_if_valid(to_select):
        try:
            res = cursor.execute(f"SELECT {to_select} FROM {table_name}")
            return res.fetchall()
        except (sqlite3.OperationalError, sqlite3.ProgrammingError) as e:
            raise EasySqlError(f"\n\nERROR: {e}") from None
    else:
        raise EasySqlError(f"\n\nERROR: table_name and to_select can only "
                           f"contain:"
                           f"\n\t- Uppercase letters (A-Z)"
                           f"\n\t- Lowercase letters (a-z)"
                           f"\n\t- Underscores"
                           f" (_).") from None
