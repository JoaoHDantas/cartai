from .fake_service import perguntar_fake
from .gemini_service import perguntar_gemini
from .anthropic_service import perguntar_claude

# Configuração para escolher o provedor de IA
#ALTERE O AI_PROVIDER PARA MUDAR A INTELIGENCIA QUE ESTA USANDO
AI_PROVIDER = "gemini"

# Opções:
# "fake"
# "gemini"
# "anthropic"


def perguntar(pergunta):

    if AI_PROVIDER == "fake":
        return perguntar_fake(pergunta)

    if AI_PROVIDER == "gemini":
        return perguntar_gemini(pergunta)

    if AI_PROVIDER == "anthropic":
        return perguntar_claude(pergunta)

    raise Exception(
        f"Provider inválido: {AI_PROVIDER}"
    )