import json
import pytest

from py_simple_package.src.py_simple.easy_json import (
    EasyJsonError,
    is_json_file,
    open_json,
    pretty_json,
    save_json_data,
    update_json,
)


class TestEasyJson:

    def test_open_json_success(self, tmp_path):
        json_file = tmp_path / "sample.json"
        data = {"name": "Sara", "role": "Maintainer", "active": True}
        json_file.write_text(json.dumps(data), encoding="utf-8")

        result = open_json(str(json_file))
        assert result == data

    def test_open_json_missing_file_raises_easy_json_error(self, tmp_path):
        missing_file = tmp_path / "does_not_exist.json"

        with pytest.raises(EasyJsonError) as exc_info:
            open_json(str(missing_file))
        assert "ERROR:" in str(exc_info.value)

    def test_open_json_invalid_syntax_raises_easy_json_error(self, tmp_path):
        bad_json_file = tmp_path / "bad_syntax.json"
        bad_json_file.write_text('{"name": "Sara",}', encoding="utf-8")

        with pytest.raises(EasyJsonError) as exc_info:
            open_json(str(bad_json_file))
        assert "ERROR:" in str(exc_info.value)

    def test_save_json_data_success(self, tmp_path):
        json_file = tmp_path / "output.json"
        data = {"project": "Py_simple", "version": "1.0.0"}

        save_json_data(str(json_file), data)

        assert json_file.exists()
        loaded_data = json.loads(json_file.read_text(encoding="utf-8"))
        assert loaded_data == data

    def test_save_json_data_already_exists_raises_easy_json_error(self, tmp_path):
        existing_file = tmp_path / "existing.json"
        existing_file.write_text('{"key": "value"}', encoding="utf-8")

        with pytest.raises(EasyJsonError) as exc_info:
            save_json_data(str(existing_file), {"new_key": "new_val"})
        assert "already exists" in str(exc_info.value)

    def test_save_json_data_invalid_directory_raises_easy_json_error(self, tmp_path):
        invalid_file = tmp_path / "non_existent_folder" / "output.json"

        with pytest.raises(EasyJsonError) as exc_info:
            save_json_data(str(invalid_file), {"key": "val"})
        assert "ERROR:" in str(exc_info.value)

    def test_pretty_json_with_dict(self):
        data = {"name": "Sara", "age": 25}
        result = pretty_json(data=data)
        assert result == json.dumps(data, indent=2)

    def test_pretty_json_with_filepath(self, tmp_path):
        json_file = tmp_path / "sample.json"
        data = {"name": "Sara", "age": 25}
        json_file.write_text(json.dumps(data), encoding="utf-8")

        result = pretty_json(filepath=str(json_file))
        assert result == json.dumps(data, indent=2)

    def test_pretty_json_no_args_raises_easy_json_error(self):
        with pytest.raises(EasyJsonError) as exc_info:
            pretty_json()
        assert "ERROR:" in str(exc_info.value)

    def test_pretty_json_both_args_raises_easy_json_error(self, tmp_path):
        json_file = tmp_path / "sample.json"
        with pytest.raises(EasyJsonError) as exc_info:
            pretty_json(data={"a": 1}, filepath=str(json_file))
        assert "ERROR:" in str(exc_info.value)

    def test_pretty_json_invalid_file_raises_easy_json_error(self, tmp_path):
        missing_file = tmp_path / "missing.json"
        with pytest.raises(EasyJsonError) as exc_info:
            pretty_json(filepath=str(missing_file))
        assert "ERROR:" in str(exc_info.value)

    def test_update_json_success(self, tmp_path):
        json_file = tmp_path / "data.json"
        initial_data = {"a": 1, "b": 2}
        json_file.write_text(json.dumps(initial_data), encoding="utf-8")

        update_json(str(json_file), {"b": 20, "c": 30})

        updated = json.loads(json_file.read_text(encoding="utf-8"))
        assert updated == {"a": 1, "b": 20, "c": 30}

    def test_update_json_missing_file_raises_easy_json_error(self, tmp_path):
        missing_file = tmp_path / "missing.json"
        with pytest.raises(EasyJsonError) as exc_info:
            update_json(str(missing_file), {"key": "val"})
        assert "ERROR:" in str(exc_info.value)

    def test_is_json_file_true(self, tmp_path):
        json_file = tmp_path / "valid.json"
        json_file.write_text("{}", encoding="utf-8")
        assert is_json_file(str(json_file)) is True

    def test_is_json_file_not_json_extension(self, tmp_path):
        txt_file = tmp_path / "valid.txt"
        txt_file.write_text("hello", encoding="utf-8")
        assert is_json_file(str(txt_file)) is False

    def test_is_json_file_does_not_exist(self, tmp_path):
        missing_file = tmp_path / "ghost.json"
        assert is_json_file(str(missing_file)) is False