from pathlib import Path

from langsmith import traceable

from kr_translator.core.generator import (
    BaseGenerator,
    ClaudeGenerator,
    GeminiGenerator,
    OpenAIGenerator,
)

_BASELINE_PROMPT = """\
# instruction
You are Korean text translator. Your job is to translate the korean text to english.
Keep the korean honorific that is commonly used, such as oppa, noona, hyung, and unnie as it is.
Translate all sound effects.

# named entities
do not translate named entities such as people's name or company name.
"""

_MEMORY_SECTION = """
# context from previous translations
Use the following summary to maintain consistency in character names, \
terminology, and writing style across translations.

{memory}
"""

_SUMMARIZE_PROMPT = """\
You are a translation assistant. Given an existing summary of previously translated \
chapters and the latest translated text, produce an updated summary.

The summary should help a translator maintain consistency across chapters. Include:
- Character names (Korean and English) and their relationships
- Recurring terminology and how it was translated
- Key plot points so far
- Notable writing style or tone choices

Aim for around 500 words. Be concise but thorough. If the existing summary is empty, \
create a new one from the translated text alone.

# existing summary
{old_summary}

# latest translated text
{new_text}

Write the updated summary now.
"""


def _get_prompt(additional="", characters="", memory=""):
    parts = [_BASELINE_PROMPT]
    if memory:
        parts.append(_MEMORY_SECTION.format(memory=memory))
    if characters:
        parts.append(characters)
    if additional:
        parts.append("# additional instruction\n" + additional)
    return "\n".join(parts)


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


_MEMORY_FILE = ".memory"


class TextTranslator:

    def __init__(
        self,
        api_key: str,
        model: str | None = None,
        model_type: str = "google",
        use_memory: bool = False,
    ):
        self.generator = _create_generator(api_key, model, model_type)
        self.use_memory = use_memory
        self.memory_path = Path(_MEMORY_FILE)

    def _read_memory(self) -> str:
        if self.use_memory and self.memory_path.exists():
            return self.memory_path.read_text(encoding="utf-8")
        return ""

    def _update_memory(self, translated_text: str) -> None:
        if not self.use_memory:
            return
        old_summary = self._read_memory()
        prompt = _SUMMARIZE_PROMPT.format(
            old_summary=old_summary or "(none)",
            new_text=translated_text,
        )
        new_summary = self.generator.generate(translated_text, prompt)
        self.memory_path.write_text(new_summary, encoding="utf-8")

    @traceable
    def translate(self, text: str, characters: str = "", additional_info: str = "") -> str:
        memory = self._read_memory()
        system_prompt = _get_prompt(additional=additional_info, characters=characters, memory=memory)
        result = self.generator.generate(text, system_prompt)
        self._update_memory(result)
        return result

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
