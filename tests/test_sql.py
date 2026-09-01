import pytest
import sqlite3
from py_simple.easy_sql import open_db, EasySqlError

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