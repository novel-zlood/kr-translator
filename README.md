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
output = translator.translate()
translator.save_translation("output_file.txt")
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
