import pytest
import sqlite3
from py_simple.easy_sql import open_db, EasySqlError, run_update

def test_open_db_success():
    """Test if the database opens successfully."""
    # SQLite has a cool trick: using ":memory:" creates a temporary 
    # database in your computer's RAM that deletes itself when finished!
    conn, cursor = open_db(":memory:")
    
    # Assert (check) that the function gave us back the right types of objects
    assert isinstance(conn, sqlite3.Connection)
    assert isinstance(cursor, sqlite3.Cursor)
    
    # Close the connection safely
    conn.close()

def test_open_db_error():
    """Test if EasySqlError is raised when given a bad path."""
    # We give it a completely impossible file path to force it to fail
    invalid_path = "/this/directory/does/not/exist/test.db"
    
    # Assert that calling the function with a bad path raises Sara's custom error
    with pytest.raises(EasySqlError):
        open_db(invalid_path)

@pytest.fixture
def users_db():
    """Sets up an in-memory database with a small users table."""
    conn, cursor = open_db(":memory:")
    cursor.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    cursor.executemany(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        [("Ada", 25), ("Grace", 40)],
    )
    conn.commit()
    yield conn, cursor
    conn.close()


def test_run_update_changes_matching_row(users_db):
    """Test that run_update only changes the row matching the condition."""
    conn, cursor = users_db

    run_update(conn, cursor, "users", {"age": 30}, "name = ?", ("Ada",))

    cursor.execute("SELECT age FROM users WHERE name = ?", ("Ada",))
    assert cursor.fetchone()[0] == 30

    # Grace's row should be untouched
    cursor.execute("SELECT age FROM users WHERE name = ?", ("Grace",))
    assert cursor.fetchone()[0] == 40


def test_run_update_multiple_columns(users_db):
    """Test that run_update can set more than one column at once."""
    conn, cursor = users_db

    run_update(conn, cursor, "users", {"name": "Ada Lovelace", "age": 36},
               "name = ?", ("Ada",))

    cursor.execute("SELECT name, age FROM users WHERE age = 36")
    row = cursor.fetchone()
    assert row == ("Ada Lovelace", 36)


def test_run_update_invalid_table_name_raises(users_db):
    """Test that an unsafe table_name raises EasySqlError instead of running."""
    conn, cursor = users_db

    with pytest.raises(EasySqlError):
        run_update(conn, cursor, "users; DROP TABLE users;", {"age": 99},
                   "name = ?", ("Ada",))


def test_run_update_invalid_column_name_raises(users_db):
    """Test that an unsafe column name in updates raises EasySqlError."""
    conn, cursor = users_db

    with pytest.raises(EasySqlError):
        run_update(conn, cursor, "users", {"age; DROP TABLE users;": 99},
                   "name = ?", ("Ada",))


def test_run_update_bad_condition_raises(users_db):
    """Test that a condition referencing a non-existent column surfaces as EasySqlError."""
    conn, cursor = users_db

    with pytest.raises(EasySqlError):
        run_update(conn, cursor, "users", {"age": 99},
                   "not_a_real_column = ?", ("Ada",))


def test_run_update_closes_connection_when_requested(users_db):
    """Test that close_conn_after=True closes the connection after updating."""
    conn, cursor = users_db

    run_update(conn, cursor, "users", {"age": 50}, "name = ?", ("Ada",),
               close_conn_after=True)

    with pytest.raises(sqlite3.ProgrammingError):
        conn.execute("SELECT 1")