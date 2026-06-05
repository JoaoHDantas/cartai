from anthropic import Anthropic
from django.conf import settings

client = Anthropic(
    api_key=settings.ANTHROPIC_API_KEY
)

def perguntar_claude(pergunta):

    resposta = client.messages.create(
        model="claude-sonnet-4",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": pergunta
            }
        ]
    )

    return resposta.content[0].text