import pytest
from py_simple.easy_json import get_nested

def test_get_nested_dict():
    data = {"a": {"b": {"c": 42}}}
    assert get_nested(data, "a.b.c") == 42
    assert get_nested(data, "a.x.y", "missing") == "missing"

def test_get_nested_list():
    data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
    assert get_nested(data, "users.0.name") == "Alice"
    assert get_nested(data, "users.2.name", "n/a") == "n/a"