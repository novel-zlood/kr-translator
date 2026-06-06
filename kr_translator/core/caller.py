from pathlib import Path

from langsmith import traceable

from kr_translator.core.generator import (
    BaseGenerator,
    ClaudeGenerator,
    GeminiGenerator,
    OpenAIGenerator,
)


def _get_prompt(additional="", characters=""):
    baseline_instructions = """
        # instruction
        You are Korean text translator. Your job is to translate the korean text to english.
        Keep the korean honorific that is commonly used, such as oppa, noona, hyung, and unnie as it is.
        Translate all sound effects.
    """

    named_entities = """
        # named entities
        do not translate named entities such as people's name or company name.
    """

    additional_instruction = """
        # additional instruction
    """
    return (
        baseline_instructions
        + named_entities
        + characters
        + additional_instruction
        + additional
    )


_GENERATOR_MAP = {
    "google": GeminiGenerator,
    "open_ai": OpenAIGenerator,
    "anthropic": ClaudeGenerator,
}


def _create_generator(api_key: str, model: str | None, model_type: str) -> BaseGenerator:
    cls = _GENERATOR_MAP.get(model_type)
    if cls is None:
        raise ValueError(
            f"Unsupported model_type: {model_type!r}. "
            f"Choose from: {', '.join(_GENERATOR_MAP)}"
        )
    if model is not None:
        return cls(api_key=api_key, model=model)
    return cls(api_key=api_key)


class TextTranslator:

    def __init__(
        self,
        api_key: str,
        model: str | None = None,
        model_type: str = "google",
    ):
        self.generator = _create_generator(api_key, model, model_type)

    @traceable
    def translate(self, text: str, characters: str = "", additional_info: str = "") -> str:
        system_prompt = _get_prompt(additional=additional_info, characters=characters)
        return self.generator.generate(text, system_prompt)

    @traceable
    def translate_file(
        self,
        source_file_location: str,
        characters: str = "",
        additional_info: str = "",
    ) -> str:
        path = Path(source_file_location)
        if not path.exists():
            raise FileNotFoundError(f"Source file not found: {source_file_location}")
        text = path.read_text(encoding="utf-8")
        return self.translate(text, characters=characters, additional_info=additional_info)

    def save_translation(
        self,
        text: str,
        destination_file_location: str = "file.txt",
        characters: str = "",
        additional_info: str = "",
    ) -> None:
        translated = self.translate(text, characters=characters, additional_info=additional_info)
        Path(destination_file_location).write_text(translated, encoding="utf-8")
