# KR Translator

Translate Korean text using LLM APIs (Google Gemini, OpenAI, Claude).

## Installation

You can install the package using pip:

```bash
pip install kr-translation
```

## Usage

### Getting GOOGLE_API_KEY

1. Go to [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey), follow instruction over there.

2. Save the API KEY somewhere safe.

### Basic Translation

```python
from kr_translator import TextTranslator

translator = TextTranslator(api_key="your_google_api_key")
output = translator.translate("안녕하세요, 오빠!")

print(output)
```

### Translate from a file

```python
from kr_translator import TextTranslator

translator = TextTranslator(api_key="your_google_api_key")
output = translator.translate_file("/path/to/file.txt")

print(output)
```

### Save Translation to a file

```python
from kr_translator import TextTranslator

translator = TextTranslator(api_key="your_google_api_key")

korean_text = open("/path/to/file.txt").read()
translator.save_translation(korean_text, "output_file.txt")
```

### Passing character information to improve translation

```python
from kr_translator import TextTranslator

translator = TextTranslator(api_key="your_google_api_key")

character_info = """
Seo Dalmi, a girl.
Nam Dosan, a boy.
Han Jipyeong, a boy, team leader at SH venture capital.
"""

output = translator.translate(
    "korean text here",
    characters=character_info,
)
```

### Passing additional information to improve translation

```python
from kr_translator import TextTranslator

translator = TextTranslator(api_key="your_google_api_key")

additional_info = """
The story revolves around startups and venture capital, therefore there are company names
that might have direct english translation, in which DO NOT translate them into english but keep
the Korean name.
"""

output = translator.translate(
    "korean text here",
    additional_info=additional_info,
)
```

### Using translation memory

Enable memory to maintain consistency across multiple translation sessions. The translator keeps a `.memory` file in the current directory that tracks character names, terminology, and plot context.

```python
from kr_translator import TextTranslator

translator = TextTranslator(api_key="your_google_api_key", use_memory=True)

# First translation creates .memory file with a summary
output1 = translator.translate("chapter 1 korean text")

# Second translation reads .memory for context, then updates it
output2 = translator.translate("chapter 2 korean text")
```

Each call makes a second LLM request to update the summary (~500 words), so character names, relationships, and terminology stay consistent across chapters.

### Using a specific Gemini model

By default, we use `gemini-2.5-flash`. You can specify a different model:

```python
from kr_translator import TextTranslator

translator = TextTranslator(
    api_key="your_google_api_key",
    model="gemini-2.5-pro",
)
output = translator.translate("korean text here")
```

### Using OpenAI model

```python
from kr_translator import TextTranslator

translator = TextTranslator(
    api_key="your_openai_api_key",
    model_type="open_ai",
    model="gpt-4o-mini",
)
output = translator.translate("korean text here")
```

### Using Claude model

```python
from kr_translator import TextTranslator

translator = TextTranslator(
    api_key="your_anthropic_api_key",
    model_type="anthropic",
)
output = translator.translate("korean text here")
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
