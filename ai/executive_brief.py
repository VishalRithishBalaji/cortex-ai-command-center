import os

from dotenv import load_dotenv
from google import genai

from ai.prompt_library import EXECUTIVE_PROMPT

# Load .env
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_brief(df):

    if df.empty:

        return "No incidents available."

    context = df.to_markdown(index=False)

    prompt = f"""

{EXECUTIVE_PROMPT}

Analytics

{context}

"""

    response = client.models.generate_content(

        model="gemini-2.0-flash",

        contents=prompt

    )

    return response.text