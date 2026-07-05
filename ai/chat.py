import os

from google import genai

from ai.prompt_library import CHAT_PROMPT

from dotenv import load_dotenv

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask(question, df):

    context = df.to_markdown(index=False)

    prompt = f"""

{CHAT_PROMPT}

Analytics

{context}

Question

{question}

"""

    response = client.models.generate_content(

        model="gemini-2.0-flash",

        contents=prompt

    )

    return response.text