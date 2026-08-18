import json
import pytest

from py_simple_package.src.py_simple.easy_json import (
    EasyJsonError,
    flatten_json,
    is_json_file,
    is_nested_json,
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

    def test_is_nested_json_true_with_dict(self):
        data = {"a": 1, "b": {"c": 2}}
        assert is_nested_json(data=data) is True

    def test_is_nested_json_true_with_list(self):
        data = {"a": 1, "b": [1, 2, 3]}
        assert is_nested_json(data=data) is True

    def test_is_nested_json_false_flat(self):
        data = {"a": 1, "b": "hello", "c": True}
        assert not is_nested_json(data=data)

    def test_is_nested_json_with_filepath(self, tmp_path):
        json_file = tmp_path / "nested.json"
        data = {"user": {"name": "Sara", "id": 101}}
        json_file.write_text(json.dumps(data), encoding="utf-8")

        assert is_nested_json(filepath=str(json_file)) is True

    def test_is_nested_json_no_args_raises_easy_json_error(self):
        with pytest.raises(EasyJsonError) as exc_info:
            is_nested_json()
        assert "ERROR:" in str(exc_info.value)

    def test_is_nested_json_both_args_raises_easy_json_error(self, tmp_path):
        json_file = tmp_path / "sample.json"
        with pytest.raises(EasyJsonError) as exc_info:
            is_nested_json(data={"a": 1}, filepath=str(json_file))
        assert "ERROR:" in str(exc_info.value)

    def test_flatten_json_dict_success(self):
        data = {"a": 1, "b": {"c": 2}}
        result = flatten_json(data=data)
        assert result == {"a": 1, "b-c": 2}

    def test_flatten_json_custom_separator(self):
        data = {"user": {"details": {"age": 25}}}
        result = flatten_json(seperator="_", data=data)
        assert result == {"user_details_age": 25}

    def test_flatten_json_with_filepath(self, tmp_path):
        json_file = tmp_path / "nested.json"
        data = {"info": {"status": "ok"}}
        json_file.write_text(json.dumps(data), encoding="utf-8")

        result = flatten_json(filepath=str(json_file))
        assert result == {"info-status": "ok"}

    def test_flatten_json_no_args_raises_easy_json_error(self):
        with pytest.raises(EasyJsonError) as exc_info:
            flatten_json()
        assert "ERROR:" in str(exc_info.value)

    def test_flatten_json_both_args_raises_easy_json_error(self, tmp_path):
        json_file = tmp_path / "sample.json"
        with pytest.raises(EasyJsonError) as exc_info:
            flatten_json(data={"a": 1}, filepath=str(json_file))
        assert "ERROR:" in str(exc_info.value)

    def test_flatten_json_list_of_scalars_uses_index_keys(self):
        data = {"a": 1, "b": [10, 20, 30]}
        result = flatten_json(data=data)
        assert result == {"a": 1, "b-0": 10, "b-1": 20, "b-2": 30}

    def test_flatten_json_list_of_dicts_joins_index_and_key(self):
        data = {"users": [{"name": "Sara"}, {"name": "Alex"}]}
        result = flatten_json(data=data)
        assert result == {"users-0-name": "Sara", "users-1-name": "Alex"}

    def test_flatten_json_list_of_dicts_custom_separator(self):
        data = {"users": [{"name": "Sara"}]}
        result = flatten_json(seperator="_", data=data)
        assert result == {"users_0_name": "Sara"}

    def test_flatten_json_nested_lists_flatten_recursively(self):
        data = {"matrix": [[1, 2], [3, 4]]}
        result = flatten_json(data=data)
        assert result == {
            "matrix-0-0": 1,
            "matrix-0-1": 2,
            "matrix-1-0": 3,
            "matrix-1-1": 4,
        }

    def test_flatten_json_dict_inside_list_inside_dict(self):
        data = {"a": {"b": [{"c": 1}]}}
        result = flatten_json(data=data)
        assert result == {"a-b-0-c": 1}

    def test_flatten_json_empty_dict_returns_empty_dict(self):
        assert flatten_json(data={}) == {}

    def test_flatten_json_already_flat_is_unchanged(self):
        data = {"a": 1, "b": "two", "c": True}
        assert flatten_json(data=data) == data

    def test_flatten_json_non_mapping_raises_easy_json_error(self):
        with pytest.raises(EasyJsonError) as exc_info:
            flatten_json(data=[1, 2, 3])
        assert "ERROR:" in str(exc_info.value)

    def test_is_nested_json_non_mapping_raises_easy_json_error(self):
        with pytest.raises(EasyJsonError) as exc_info:
            is_nested_json(data=[1, 2, 3])
        assert "ERROR:" in str(exc_info.value)

    def test_is_nested_json_empty_dict_is_not_nested(self):
        assert not is_nested_json(data={})

    def test_is_nested_json_invalid_file_raises_easy_json_error(self, tmp_path):
        bad_file = tmp_path / "bad.json"
        bad_file.write_text("{not json}", encoding="utf-8")
        with pytest.raises(EasyJsonError) as exc_info:
            is_nested_json(filepath=str(bad_file))
        assert "ERROR:" in str(exc_info.value)

    def test_flatten_json_invalid_file_raises_easy_json_error(self, tmp_path):
        bad_file = tmp_path / "bad.json"
        bad_file.write_text("{not json}", encoding="utf-8")
        with pytest.raises(EasyJsonError) as exc_info:
            flatten_json(filepath=str(bad_file))
        assert "ERROR:" in str(exc_info.value)

    def test_update_json_preserves_untouched_keys(self, tmp_path):
        json_file = tmp_path / "data.json"
        json_file.write_text(
            json.dumps({"keep": "me", "change": "old"}), encoding="utf-8"
        )

        update_json(str(json_file), {"change": "new"})

        assert json.loads(json_file.read_text(encoding="utf-8")) == {
            "keep": "me",
            "change": "new",
        }

    def test_save_then_open_json_round_trip(self, tmp_path):
        json_file = tmp_path / "round_trip.json"
        data = {"nested": {"list": [1, 2]}, "flag": False, "nothing": None}

        save_json_data(str(json_file), data)

        assert open_json(str(json_file)) == data

    def test_is_json_file_uppercase_extension_is_rejected(self, tmp_path):
        json_file = tmp_path / "valid.JSON"
        json_file.write_text("{}", encoding="utf-8")
        assert is_json_file(str(json_file)) is False

    def test_is_json_file_directory_is_not_a_file(self, tmp_path):
        assert is_json_file(str(tmp_path)) is False