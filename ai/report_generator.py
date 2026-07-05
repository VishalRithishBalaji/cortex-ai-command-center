import os

from google import genai

from ai.prompt_library import REPORT_PROMPT

from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate(df):

    context = df.to_markdown(index=False)

    prompt = f"""

{REPORT_PROMPT}

Analytics

{context}

"""

    response = client.models.generate_content(

        model="gemini-2.0-flash",

        contents=prompt

    )

    return response.text