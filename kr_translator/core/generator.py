from abc import ABC, abstractmethod

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser


class BaseGenerator(ABC):

    @abstractmethod
    def generate(self, text: str, system_prompt: str) -> str:
        ...

    def _invoke_chain(self, llm, text: str, system_prompt: str) -> str:
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        chain = prompt | llm | StrOutputParser()
        return chain.invoke({"input": text})


class GeminiGenerator(BaseGenerator):

    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        from langchain_google_genai import ChatGoogleGenerativeAI

        self.llm = ChatGoogleGenerativeAI(google_api_key=api_key, model=model)

    def generate(self, text: str, system_prompt: str) -> str:
        return self._invoke_chain(self.llm, text, system_prompt)


class OpenAIGenerator(BaseGenerator):

    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        from langchain_openai.chat_models import ChatOpenAI

        self.llm = ChatOpenAI(openai_api_key=api_key, model=model)

    def generate(self, text: str, system_prompt: str) -> str:
        return self._invoke_chain(self.llm, text, system_prompt)


class ClaudeGenerator(BaseGenerator):

    def __init__(self, api_key: str, model: str = "claude-sonnet-4-6-20250514"):
        from langchain_anthropic import ChatAnthropic

        self.llm = ChatAnthropic(anthropic_api_key=api_key, model=model)

    def generate(self, text: str, system_prompt: str) -> str:
        return self._invoke_chain(self.llm, text, system_prompt)
