import os
import pytest
import re
from unittest.mock import patch, mock_open
from kr_translator.caller import TextTranslator


def contains_korean(text):
    korean_pattern = re.compile(r'[\u3131-\u3163\uac00-\ud7a3]')
    return bool(korean_pattern.search(text))


@pytest.mark.call_openai
def test_translate(source_test_file):
    translator = TextTranslator(api_key=os.environ["OPENAI_API_KEY"], source_file_location=source_test_file)
    output = translator.translate()

    assert isinstance(output, str)
    assert len(output) > 100


@pytest.mark.call_openai
def test_translate_sound(sound_test_file):
    translator = TextTranslator(api_key=os.environ["OPENAI_API_KEY"], source_file_location=sound_test_file)
    output = translator.translate()

    assert not contains_korean(output)


def test_translate_invalid_file():
    with pytest.raises(ValueError, match="The source file must be a .txt file"):
        TextTranslator(api_key="test_api_key", source_file_location="test.pdf")


@patch('kr_translator.caller.open', new_callable=mock_open)
@patch('kr_translator.caller.TextTranslator.translate', return_value="Some translated English text")
def test_save_translation(mock_translate, mock_file):
    translator = TextTranslator(api_key="test_api_key", source_file_location="test.txt")
    translator.save_translation("destination.txt")

    mock_translate.assert_called_once()
    mock_file.assert_called_once_with("destination.txt", "w")
    mock_file().write.assert_called_once_with("Some translated English text")
