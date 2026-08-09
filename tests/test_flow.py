"""Tests for easy_flow module."""

import time

import pytest

from py_simple_package.src.py_simple.easy_flow import (
    EasyFlowError,
    retry,
    run_py_file,
    run_py_file_safe,
    time_function_call,
    time_it,
)


class TestEasyFlowError:
    """Tests for the EasyFlowError exception."""

    def test_is_exception(self):
        """Should be a regular Exception subclass."""
        assert issubclass(EasyFlowError, Exception)

    def test_stores_message(self):
        """Should store and display the given message."""
        err = EasyFlowError("something broke")
        assert err.message == "something broke"
        assert str(err) == "something broke"


class TestRunPyFile:
    """Tests for run_py_file function."""

    def test_runs_successfully(self, tmp_path, capsys):
        """Should run the file and let its output through."""
        script = tmp_path / "script.py"
        script.write_text("print('hello from script')\n")

        run_py_file(str(script))

        captured = capsys.readouterr()
        assert "RUNNING:" in captured.out
        assert "hello from script" in captured.out

    def test_missing_file_raises(self):
        """Should raise EasyFlowError for a file that doesn't exist."""
        with pytest.raises(EasyFlowError):
            run_py_file("does_not_exist.py")

    def test_script_error_raises(self, tmp_path):
        """Should wrap an exception raised inside the script."""
        script = tmp_path / "broken.py"
        script.write_text("raise ValueError('boom')\n")

        with pytest.raises(EasyFlowError) as exc_info:
            run_py_file(str(script))
        assert "boom" in str(exc_info.value)


class TestRunPyFileSafe:
    """Tests for run_py_file_safe function."""

    def test_runs_successfully(self, tmp_path, capsys):
        """Should return (True, None) and print progress on success."""
        script = tmp_path / "script.py"
        script.write_text("print('all good')\n")

        success, error = run_py_file_safe(str(script))

        assert success is True
        assert error is None
        captured = capsys.readouterr()
        assert "RUNNING:" in captured.out

    def test_missing_file_returns_error(self):
        """Should return (False, message) instead of raising."""
        success, error = run_py_file_safe("does_not_exist.py")
        assert success is False
        assert error is not None

    def test_script_error_returns_error(self, tmp_path):
        """Should capture an exception raised inside the script."""
        script = tmp_path / "broken.py"
        script.write_text("raise ValueError('boom')\n")

        success, error = run_py_file_safe(str(script))

        assert success is False
        assert "boom" in error


class TestTimeFunctionCall:
    """Tests for time_function_call function."""

    def test_returns_a_float(self):
        """Should return a non-negative float duration."""
        duration = time_function_call(lambda: "done")
        assert isinstance(duration, float)
        assert duration >= 0

    def test_calls_function_with_args(self):
        """Should call the function with the given positional args."""
        calls = []

        def add(a, b):
            calls.append((a, b))
            return a + b

        time_function_call(add, [2, 3])
        assert calls == [(2, 3)]

    def test_calls_function_with_no_args(self):
        """Should call the function with no arguments when args is None."""
        calls = []

        def no_args():
            calls.append(True)

        time_function_call(no_args)
        assert calls == [True]

    def test_measures_elapsed_time(self, monkeypatch):
        """Should report the difference between start and end time."""
        times = iter([100.0, 100.5])
        monkeypatch.setattr(time, "time", lambda: next(times))

        duration = time_function_call(lambda: None)
        assert duration == pytest.approx(0.5)

    def test_function_error_raises_easyflowerror(self):
        """Should wrap an exception raised by the function."""
        def boom():
            raise ValueError("bad function")

        with pytest.raises(EasyFlowError) as exc_info:
            time_function_call(boom)
        assert "bad function" in str(exc_info.value)


class TestTimeIt:
    """Tests for the time_it decorator."""

    def test_returns_original_result(self):
        """Should return whatever the wrapped function returns."""
        @time_it
        def add(a, b):
            return a + b

        assert add(2, 3) == 5

    def test_prints_timing(self, capsys):
        """Should print the function's name and elapsed time."""
        @time_it
        def add(a, b):
            return a + b

        add(2, 3)

        captured = capsys.readouterr()
        assert "add took" in captured.out

    def test_supports_args_and_kwargs(self):
        """Should forward both positional and keyword arguments."""
        @time_it
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        assert greet("World", greeting="Hi") == "Hi, World!"


class TestRetry:
    """Tests for the retry function."""

    def test_succeeds_on_first_try(self, monkeypatch):
        """Should return the result immediately if there's no failure."""
        monkeypatch.setattr(time, "sleep", lambda s: None)
        calls = []

        def always_works():
            calls.append(1)
            return "success"

        result = retry(always_works)
        assert result == "success"
        assert len(calls) == 1

    def test_succeeds_after_some_failures(self, monkeypatch):
        """Should keep retrying until the function succeeds."""
        monkeypatch.setattr(time, "sleep", lambda s: None)
        calls = []

        def fails_twice_then_works():
            calls.append(1)
            if len(calls) < 3:
                raise ValueError("not yet")
            return "success"

        result = retry(fails_twice_then_works, attempts=5)
        assert result == "success"
        assert len(calls) == 3

    def test_raises_after_all_attempts_fail(self, monkeypatch):
        """Should raise the last exception once attempts are exhausted."""
        monkeypatch.setattr(time, "sleep", lambda s: None)
        calls = []

        def always_fails():
            calls.append(1)
            raise ValueError("nope")

        with pytest.raises(ValueError, match="nope"):
            retry(always_fails, attempts=3)
        assert len(calls) == 3

    def test_waits_between_attempts(self, monkeypatch):
        """Should sleep for `delay` seconds between failed attempts."""
        sleep_calls = []
        monkeypatch.setattr(time, "sleep", lambda s: sleep_calls.append(s))

        def always_fails():
            raise ValueError("nope")

        with pytest.raises(ValueError):
            retry(always_fails, attempts=3, delay=2)

        assert sleep_calls == [2, 2]

    def test_default_attempts_and_delay(self, monkeypatch):
        """Should default to 3 attempts and a 1 second delay."""
        sleep_calls = []
        monkeypatch.setattr(time, "sleep", lambda s: sleep_calls.append(s))
        calls = []

        def always_fails():
            calls.append(1)
            raise ValueError("nope")

        with pytest.raises(ValueError):
            retry(always_fails)

        assert len(calls) == 3
        assert sleep_calls == [1, 1]
