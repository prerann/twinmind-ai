from groq import Groq
from config.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_response(messages):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"