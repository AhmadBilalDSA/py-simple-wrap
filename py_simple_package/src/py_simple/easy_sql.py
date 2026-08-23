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
    """Check that a table/column string is safe to interpolate into SQL."""
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
    try:
        conn = sqlite3.connect(db_filepath)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.OperationalError as e:
        raise EasySqlError(f"\n\nERROR: {e}") from None


def run_select(connection: sqlite3.Connection, cursor: sqlite3.Cursor ,
               table_name: str, to_select: str):
    """
    Runs a SELECT query against a table and returns all matching rows.

    Validates `table_name` and `to_select` first — only letters, numbers,
    and underscores are allowed (or `*` for `to_select`) — to guard
    against SQL injection before building the query string.

    Args:
        connection (sqlite3.Connection): Open connection to the database.
        cursor (sqlite3.Cursor): Cursor for executing SQL statements.
        table_name (str): Name of the table to select from.
        to_select (str): Column name(s) to select, comma-separated, or
            "*" for all columns.

    Returns:
        list[tuple]: All rows returned by the query.

    Raises:
        EasySqlError: If `table_name` or `to_select` contain anything
            other than letters, numbers, underscores, or "*", or if the
            query itself fails.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import open_db, run_select

            connection, cursor = open_db('mydb.db')
            rows = run_select(connection, cursor, 'users', 'name, email')
            ```

        === "The Traditional Way"
            ```python
            import sqlite3

            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            rows = cursor.execute("SELECT name, email FROM users").fetchall()
            ```
    """
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
                           f"\n\t- Underscores  (_).") from None


def run_insert():
    pass