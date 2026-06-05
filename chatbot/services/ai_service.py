from .anthropic_service import perguntar_claude

USE_FAKE_AI = True


def perguntar(pergunta):

    if USE_FAKE_AI:
        return resposta_fake(pergunta)

    return perguntar_claude(pergunta)


def resposta_fake(pergunta):

    return f"""
[MODO TESTE]

Você perguntou:

{pergunta}

Quando a API estiver ativa,
a resposta virá do Claude.
"""