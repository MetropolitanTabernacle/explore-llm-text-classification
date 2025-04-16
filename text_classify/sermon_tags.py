from .llms import LLMFactory


try:
    # Gemini
    gemini_instance = LLMFactory.create_llm("gemini", "gemini-2.0-flash")
    gemini_response = gemini_instance.generate_text("Explain how AI works")
    print("Gemini Response:", gemini_response)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occured {e}")