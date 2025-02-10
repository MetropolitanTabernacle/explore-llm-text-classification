from openai import OpenAI
from decouple import config

OpenAI_API_KEY = config("OPENAI_API_KEY")
client = OpenAI(api_key=OpenAI_API_KEY)

# simulate modules that'll be created in the near future.
content_categories = ["faith", "hope", "love"]
system_content = f"You are a helpful assistant. When the user inputs content, your task is to return a response categorising the user's input content as on of these categories {content_categories} and suggesting another one word category that could described the content, if that category is not in the provided list. Your result should be in dict format where the keys are category_choice and category_suggestion. Go straight to the point"
user_content ="""
I love the LORD, because He has heard My voice and my supplications. Because He has inclined His ear to me, Therefore I will call upon Him as long as I live. The pains of death surrounded me, And the pangs of Sheol laid hold of me; I found trouble and sorrow. Then I called upon the name of the LORD: “O LORD, I implore You, deliver my soul!” Gracious is the LORD, and righteous; Yes, our God is merciful. The LORD preserves the simple; I was brought low, and He saved me. Return to your rest, O my soul, For the LORD has dealt bountifully with you. For You have delivered my soul from death, My eyes from tears, And my feet from falling. I will walk before the LORD In the land of the living. I believed, therefore I spoke, “I am greatly afflicted.” I said in my haste, “All men are liars.” What shall I render to the LORD For all His benefits toward me? I will take up the cup of salvation, And call upon the name of the LORD. I will pay my vows to the LORD Now in the presence of all His people. Precious in the sight of the LORD Is the death of His saints. O LORD, truly I am Your servant; I am Your servant, the son of Your maidservant; You have loosed my bonds.
"""

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_content},
        {
            "role": "user",
            "content": user_content,
        }
    ]
)

print(completion.choices[0].message)