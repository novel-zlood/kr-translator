import os
import re
from unittest.mock import patch

import pytest

from kr_translator.core.caller import TextTranslator
from kr_translator.core.utils import has_repeating_chars


def contains_korean(text):
    korean_pattern = re.compile(r"[ㄱ-ㅣ가-힣]")
    return bool(korean_pattern.search(text))


@pytest.fixture()
def mock_translator():
    translator = TextTranslator(api_key="fake-key")
    return translator


# --- Unit tests (no API calls) ---


def test_translate(mock_translator):
    with patch.object(
        mock_translator.generator, "generate", return_value="Hello, oppa!"
    ):
        output = mock_translator.translate("안녕, 오빠!")

    assert output == "Hello, oppa!"


def test_translate_passes_system_prompt(mock_translator):
    with patch.object(
        mock_translator.generator, "generate", return_value="translated"
    ) as mock_gen:
        mock_translator.translate(
            "text", characters="Kim Yuna, a girl.", additional_info="Fantasy novel"
        )

    _, kwargs = mock_gen.call_args
    system_prompt = kwargs.get("system_prompt") or mock_gen.call_args[0][1]
    assert "Kim Yuna, a girl." in system_prompt
    assert "Fantasy novel" in system_prompt


def test_translate_file(mock_translator, source_test_file):
    with patch.object(
        mock_translator.generator, "generate", return_value="Translated text"
    ):
        output = mock_translator.translate_file(source_file_location=source_test_file)

    assert output == "Translated text"


def test_translate_file_not_found():
    translator = TextTranslator(api_key="test_api_key")
    with pytest.raises(FileNotFoundError):
        translator.translate_file(source_file_location="nonexistent.txt")


def test_save_translation(mock_translator, tmp_path):
    dest = tmp_path / "output.txt"
    with patch.object(
        mock_translator.generator, "generate", return_value="Saved translation"
    ):
        mock_translator.save_translation("korean text", str(dest))

    assert dest.read_text() == "Saved translation"


def test_unsupported_model_type():
    with pytest.raises(ValueError, match="Unsupported model_type"):
        TextTranslator(api_key="test_api_key", model_type="invalid")


def test_openai_model_type():
    translator = TextTranslator(
        api_key="fake-key", model_type="open_ai", model="gpt-4o-mini"
    )
    assert translator.generator is not None


def test_anthropic_model_type():
    translator = TextTranslator(
        api_key="fake-key", model_type="anthropic"
    )
    assert translator.generator is not None


# --- Integration tests (require API keys) ---


@pytest.mark.call_openai
def test_translate_openai_integration(source_text):
    translator = TextTranslator(
        api_key=os.environ["OPENAI_API_KEY"],
        model_type="open_ai",
    )
    output = translator.translate(text=source_text)

    assert isinstance(output, str)
    assert len(output) > 100


@pytest.mark.call_openai
def test_translate_sound_openai(sound_test_file):
    translator = TextTranslator(
        api_key=os.environ["OPENAI_API_KEY"],
        model_type="open_ai",
    )
    output = translator.translate_file(source_file_location=sound_test_file)

    assert not contains_korean(output)


@pytest.mark.call_openai
def test_translate_gemini_integration(source_text):
    translator = TextTranslator(
        api_key=os.environ["GOOGLE_API_KEY"],
    )
    output = translator.translate(text=source_text)

    assert isinstance(output, str)
    assert len(output) > 100


@pytest.mark.call_openai
def test_translate_no_repeating_chars(source_text):
    translator = TextTranslator(
        api_key=os.environ["GOOGLE_API_KEY"],
    )
    output = translator.translate(text=source_text)

    assert not has_repeating_chars(output)


@pytest.mark.call_openai
def test_translate_sound_gemini(sound_test_file):
    translator = TextTranslator(
        api_key=os.environ["GOOGLE_API_KEY"],
    )
    output = translator.translate_file(source_file_location=sound_test_file)

    assert not contains_korean(output)
