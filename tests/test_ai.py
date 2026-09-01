import pytest
from unittest.mock import MagicMock
from py_simple.easy_ai import summarize_text, EasyAIError


def test_summarize_text_success():
    """Test that summarize_text correctly returns model response content."""
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.content = "Summary result content."
    mock_model.invoke.return_value = mock_response

    result = summarize_text(mock_model, "Some text to summarize.")

    assert result == "Summary result content."
    mock_model.invoke.assert_called_once()


def test_summarize_text_error():
    """Test that summarize_text wraps execution errors in EasyAIError."""
    mock_model = MagicMock()
    mock_model.invoke.side_effect = Exception("Model timeout")

    with pytest.raises(EasyAIError) as exc_info:
        summarize_text(mock_model, "Some text")

    assert "Model timeout" in str(exc_info.value)