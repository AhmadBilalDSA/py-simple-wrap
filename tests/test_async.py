import pytest

from py_simple_package.src.py_simple.easy_async import (
    EasyAsyncError,
    run_at_the_same_time_no_params,
    run_at_the_same_time_with_params,
)


def test_run_at_the_same_time_no_params_error():
    def failing_function():
        raise ValueError("Something went wrong")

    with pytest.raises(EasyAsyncError):
        run_at_the_same_time_no_params([failing_function])


def test_run_at_the_same_time_no_params():
    def add():
        return 2 + 2

    def multiply():
        return 3 * 3

    result = run_at_the_same_time_no_params([add, multiply])

    assert result == [
        ("add", 4),
        ("multiply", 9),
    ]


def test_run_at_the_same_time_with_params():
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    result = run_at_the_same_time_with_params([
        (add, 5, 3),
        (subtract, 5, 3),
    ])

    assert result == [
        ("add", 8),
        ("subtract", 2),
    ]


def test_run_at_the_same_time_with_params_error():
    def failing_function(value):
        raise ValueError("Something went wrong")

    with pytest.raises(EasyAsyncError):
        run_at_the_same_time_with_params([
            (failing_function, 10)
        ])