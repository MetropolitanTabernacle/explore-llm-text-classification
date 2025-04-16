from abc import ABC, abstractmethod
from decouple import config
from openai import OpenAI
import google.generativeai as genai

from typing import Optional

class LLMInterface(ABC):
    """Abstract interface for Language Model interactions."""

    @abstractmethod
    def generate_text(self, prompt:str, system_prompt: Optional[str]=None) -> Optional[str]:
        """Generates text based on the provided prompt."""
        pass

class ChatGPTModel(LLMInterface):
    """Implements ChatGPT model calls."""

    def __init__(self, model_name: str) -> None:
        self.client = OpenAI(api_key=config("OPENAI_API_KEY"))
        self.model_name = model_name

    def generate_text(self, prompt: str, system_prompt: Optional[str]=None) -> Optional[str]:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        completion = self.client.chat.completions.create(model=self.model_name, messages=messages)
        return completion.choices[0].message.content

class GeminiModel(LLMInterface):
    """Implements Gemini model calls."""

    def __init__(self, model_name:str) -> None:
        genai.configure(api_key=config("GEMINI_API_KEY"))
        self.client = genai.GenerativeModel(model_name=model_name)

    def generate_text(self, prompt: str, system_prompt: Optional[str]=None) -> str:
        response = self.client.generate_content(prompt)
        return response.text

class LLMFactory:
    """Factory for creating LLM instances."""

    @staticmethod
    def create_llm(api_name: str, model_name: str) -> ChatGPTModel|GeminiModel|ValueError: # extremely hacky return type annotation. to rewrite.
        if api_name.lower() == "chatgpt":
            return ChatGPTModel(model_name)
        elif api_name.lower() == "gemini":
            return GeminiModel(model_name)
        else:
            raise ValueError(f"Unsupported API: {api_name}")
