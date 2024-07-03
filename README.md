# KR Translator

Translate a korean `txt` file.

## Installation

You can install the package using pip:

```bash
pip install kr-translation
```

## Usage

### Getting OPENAI API KEY

1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys), follow instruction over there.

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

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
