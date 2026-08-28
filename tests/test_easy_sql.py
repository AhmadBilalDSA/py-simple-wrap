import pytest
from unittest.mock import patch, MagicMock
import sys, os
sys.path.insert(0, os.path.abspath("src"))
from py_simple import easy_sql

def test_easy_sql_module_exists():
    assert easy_sql is not None

def test_easy_sql_query_execution_mock():
    with patch("sqlite3.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [("test_row",)]
        res = easy_sql.execute_query("dummy.db", "SELECT 1")
        assert len(res) == 1
        assert res[0] == ("test_row",)
