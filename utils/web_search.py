import requests

def search_web(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url).json()

        if response.get("AbstractText"):
            return response["AbstractText"]

        return "No relevant web results found."

    except Exception as e:
        return f"Web search error: {str(e)}"