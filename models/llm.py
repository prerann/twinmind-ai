from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEYS"])

def generate_response(messages):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"