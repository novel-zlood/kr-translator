from langchain_community.callbacks import get_openai_callback
from langchain_community.document_loaders.text import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers.string import StrOutputParser

from kr_translator.exceptions import TextLoaderError


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


class TextTranslator:
    """
    A class used to translate text from a source file using the OpenAI API.

    Attributes:
        api_key (str): The API key for accessing OpenAI services.
        source_file_location (str): The location of the source text file to be translated.

    Methods:
        translate(characters="", additional_info=""): Translates the text from the source file using the specified characters and additional information.
        save_translation(destination_file_location="file.txt"): Saves the translated text to the specified destination file location.
    """

    def __init__(self, api_key, source_file_location):
        if not source_file_location.endswith(".txt"):
            raise ValueError("The source file must be a .txt file")
        self.llm = ChatOpenAI(
            openai_api_key=api_key,
            model="gpt-4o",
        )
        self.source_file_location = source_file_location

    def translate(self, characters="", additional_info=""):
        """
        Translates the text from the source file using the specified characters and additional information.

        Args:
            characters (str, optional): Specific characters or personalities to use in the translation. Defaults to "".
            additional_info (str, optional): Additional information or context to provide to the translation model. Defaults to "".

        Returns:
            str: The translated text.

        Raises:
            TextLoaderError: If the source file cannot be loaded.
        """
        try:
            loader = TextLoader(self.source_file_location)
            document = loader.load()
        except Exception as e:
            raise TextLoaderError(
                f"Failed to load the file {self.source_file_location}"
            ) from e

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    _get_prompt(additional=additional_info, characters=characters),
                ),
                ("human", "{input}"),
            ]
        )
        parser = StrOutputParser()

        chain = prompt | self.llm | parser

        with get_openai_callback() as cb:
            output = chain.invoke({"input": document})
            print(f"Total Tokens: {cb.total_tokens}")
            print(f"Prompt Tokens: {cb.prompt_tokens}")
            print(f"Completion Tokens: {cb.completion_tokens}")
            print(f"Total Cost (USD): ${cb.total_cost}")

            return output

    def save_translation(self, destination_file_location: str = "file.txt"):
        """
        Saves the translated text to the specified destination file location.

        Args:
            destination_file_location (str, optional): The location to save the translated text file. Defaults to "file.txt".
        """
        translated_text = self.translate()

        with open(destination_file_location, "w") as file:
            file.write(translated_text)
