from django.shortcuts import render
from .services.ai_service import perguntar


def chat_view(request):

    resposta = None

    if request.method == "POST":
        pergunta = request.POST.get("pergunta")

        if pergunta:
            resposta = perguntar(pergunta)

    return render(
        request,
        "chatbot/chat.html",
        {
            "resposta": resposta
        }
    )