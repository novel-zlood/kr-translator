from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


def _get_prompt(additional="", characters=""):
    baseline_instructions = """
        # instruction
        You are Korean text translator. Your job is to translate the korean text to english.
        Translate all written sound effects.
    """

    named_entities = """
        # named entities
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


class HuggingFaceTranslator:
    def __init__(self, model="LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct"):
        self.llm = ChatHuggingFace(
            llm=HuggingFacePipeline.from_model_id(
                model_id=model,
                task="text-generation",
                pipeline_kwargs=dict(
                    max_new_tokens=512,
                    do_sample=False,
                    repetition_penalty=1.03,
                ),
            )
        )

    def translate(self, characters="", additional_info="", text=""):
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
        output = chain.invoke({"input": text})

        return output
