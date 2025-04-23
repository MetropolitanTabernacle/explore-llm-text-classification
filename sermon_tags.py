from text_classify import LLMFactory
from input_data import sermons

tagging_instructions = """You are a helpful assistant. 
read the text you've been given and draw out three key themes, one word each.
your result should be a python list of the one-word themes, each a string, gotten from analysing the text.
Go straight to the point"""

for filename, sermon_text in sermons.items():
    try:
        # Gemini
        gemini_instance = LLMFactory.create_llm("gemini", "gemini-2.0-flash")
        gemini_response = gemini_instance.generate_text(
            sermon_text, tagging_instructions
        )
        print(f"{filename}: {gemini_response}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occured {e}")
