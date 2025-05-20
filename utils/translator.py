import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_to_hindi(text):
    system_prompt = (
    "You are a skilled Hindi translator. Translate the following English spiritual text "
    "into **clear, natural, and friendly Hindi**, as if speaking to a curious elder parent. "
    "Avoid overly formal or poetic language. Keep it respectful, gentle, and easy to read aloud."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content
