from openai import OpenAI
from decouple import config

OpenAI_API_KEY = config("OPENAI_API_KEY")
client = OpenAI(api_key=OpenAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "suggest a one-word category that describes Psalm 116",
        }
    ]
)

print(completion.choices[0].message)