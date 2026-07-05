import os
import json

from google import genai
from dotenv import load_dotenv

from PIL import Image
import json

from ai.prompt import PROMPT

from ai.schemas import DecisionReport
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

from pydantic import BaseModel

class IncidentReport(BaseModel):

    incident_type: str

    confidence: float

    severity: int

    description: str

    department: str

    recommendation: str

from PIL import Image

def analyze(image_path):

    image = Image.open(image_path)

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=[image, PROMPT],

        config={

            "response_mime_type":"application/json",

            "response_schema":DecisionReport

        }

    )

    return json.loads(response.text)