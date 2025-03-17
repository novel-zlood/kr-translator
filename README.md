# KR Translator

Translate a korean `txt` file.

## Installation

You can install the package using pip:

```bash
pip install kr-translation
```

## Usage

### Getting GOOGLE_API_KEU

1. Go to [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey), follow instruction over there.

2. Save the API KEY somewhere save.

### Basic Translation

```python
from kr_translator.caller import TextTranslator

translator = TextTranslator(
  api_key="your_api_key_here", 
  source_file_location="/path/to/file.txt"
)
output = translator.translate()

print(output)
```

### Save Translation to a file

```python
from kr_translator.caller import TextTranslator

translator = TextTranslator(
  api_key="your_api_key_here", 
  source_file_location="/path/to/file.txt"
)
translator.save_translation("output_file.txt")
```

### Passing character information to improve translation

```python
from kr_translator.caller import TextTranslator

translator = TextTranslator(
  api_key="your_api_key_here", 
  source_file_location="/path/to/file.txt"
)

character_info = """
Seo Dalmi, a girl.
Nam Dosan, a boy.
Han Jipyeong, a boy, team leader at SH venture capital.
"""

translator.save_translation(
    destination_file_location="output_file.txt",
    characters=character_info
)
```

### Passing additional information to improve translation

```python
from kr_translator.caller import TextTranslator

translator = TextTranslator(
  api_key="your_api_key_here", 
  source_file_location="/path/to/file.txt"
)

additonal_info = """
The story revolve around startups and venture capital, therefore there is gonna be company name
that might have direct english translation, in which DO NOT translate them into english but keep
the Korean name.
"""

translator.save_translation(
    destination_file_location="output_file.txt",
    additional_info=additonal_info
)
```

### Using different Gemini model

By default, we are using experimental `gemini-2.0-flash-exp`, because it is a free model. However it comes with strict rate limit. Once we reach this limit, we need to use paid model such as `gemini-2.0-flash`.

```python
from kr_translator.caller import TextTranslator

translator = TextTranslator(
  api_key="your_api_key_here", 
  source_file_location="/path/to/file.txt",
  model="gemini-2.0-flash"
)
output = translator.translate()

print(output)
```

### Using OpenAI model

In order to use OpenAI model, we need OPENAI_API_KEY. Go to [this page](https://platform.openai.com/api-keys) to get it.

```python
from kr_translator.caller import TextTranslator

translator = TextTranslator(
  api_key="your_openai_api_key_here", 
  source_file_location="/path/to/file.txt",
  model_type="open_ai",
  model="gpt-4o-mini",  # required when model_type is open_ai
)
output = translator.translate()

print(output)
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
