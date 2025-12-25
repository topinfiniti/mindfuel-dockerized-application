import requests
from datetime import datetime
import os

def extract_quote():
    try:
        response = requests.get(
            os.getenv("ZENQUOTE_API_URL"),
            timeout=10
        )

        if response.status_code != 200:
            raise Exception(f"Bad status code: {response.status_code}")

        if not response.text.strip():
            raise Exception("Empty response from API")

        data = response.json()

        if not isinstance(data, list) or len(data) == 0:
            raise Exception("Unexpected API response format")

        quote = data[0].get("q")
        author = data[0].get("a")

        return quote, author

    except Exception as e:
        print(f"Error fetching quote: {e}")
        return None, None
