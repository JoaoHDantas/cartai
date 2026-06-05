from google import genai
from django.conf import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def perguntar_gemini(pergunta):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=pergunta
    )

    return response.text