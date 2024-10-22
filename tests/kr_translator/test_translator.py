import os
import pytest
import re
from unittest.mock import patch, mock_open
from kr_translator.translator import HuggingFaceTranslator


def contains_korean(text):
    korean_pattern = re.compile(r'[\u3131-\u3163\uac00-\ud7a3]')
    return bool(korean_pattern.search(text))


def test_translate_huggingface(source_text):
    translator = HuggingFaceTranslator()
    output = translator.translate(text=source_text)

    assert isinstance(output, str)
    assert len(output) > 100


# def test_translate_sound(sound_test_file):
#     translator = TextTranslator(api_key=os.environ["OPENAI_API_KEY"], source_file_location=sound_test_file)
#     output = translator.translate()
#
#     assert not contains_korean(output)